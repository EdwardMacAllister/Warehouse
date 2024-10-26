from sqlalchemy.orm import Session
from Bot.database.models import DailyReport


def create_daily_report(db: Session, report_date: str, details: str):
    """Create a new daily report."""
    new_report = DailyReport(report_date=report_date, details=details)
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    return new_report


def delete_daily_report(db: Session, report_id: int) -> bool:
    """Delete a daily report by ID."""
    report = db.query(DailyReport).filter(DailyReport.id == report_id).one_or_none()
    if report:
        db.delete(report)
        db.commit()
        return True
    return False


def list_daily_reports(db: Session):
    """List all daily reports."""
    return db.query(DailyReport).all()
