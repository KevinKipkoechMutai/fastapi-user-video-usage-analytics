from fastapi import APIRouter, Query
from typing import List, Optional
from models import UserActivity, UserGroup
from dependencies import db_dependency
from sqlalchemy import func

# Function to split date
def split_date(report_date):
    if report_date is None or len(report_date) != 8 or not report_date.isdigit():
        print(f"Invalid date format for value: {report_date}")
        raise ValueError("Invalid date format. Expected YYYYMMDD.")
    
    year = report_date[:4]
    month = report_date[4:6]
    day = report_date[6:8]
    
    return year, month, day

router = APIRouter()

@router.get("/analytics")
def get_analytics(
    db: db_dependency,
    group_ids: Optional[List[int]] = Query(None),
    period: str = Query("year", regex="^(year|month)$")  # Only allow "year"
):
    try:
        query = (
            db.query(
                UserGroup.group_name,
                func.sum(UserActivity.watched_seconds / 3600).label("watched_hours"),
                func.strftime("%Y", UserActivity.report_date_yyyymmdd if period == "year" else "%Y-%m")
            )
            .join(UserActivity, UserActivity.user_id == UserGroup.user_id)
        )

        if group_ids:
            query = query.filter(UserGroup.group_id.in_(group_ids))

        if period == "year":
            query = query.group_by(UserGroup.group_name, func.strftime("%Y", UserActivity.report_date_yyyymmdd))
        else:
            query = query.group_by(UserGroup.group_name, func.strftime("%Y-%m", UserActivity.report_date_yyyymmdd))

        results = query.all()

        data = [
            {
                "group_name": row[0],
                "watched_hours": row[1],
                "period": row[2]
            }
            for row in results
        ]

        return {"period": period, "data": data}
    finally:
        db.close()