from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DailyReport(Base):
    __tablename__ = 'daily_reports'

    id = Column(Integer, primary_key=True, index=True)
    report_date = Column(DateTime)
    details = Column(String)
    branch_id = Column(Integer, ForeignKey('branches.id'))  # Assuming this is a foreign key to a Branch

    def __repr__(self):
        return f"<DailyReport(report_date={self.report_date}, details={self.details})>"
