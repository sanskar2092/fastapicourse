from sqlalchemy.orm import Session
from repository.jobs import create_new_job, retrieve_job
from schemas.jobs import JobCreate
from tests.utils.users import create_random_owner


def test_retrieve_job_by_id(db_session: Session):
    title = "test_title_1"
    company = "test_company_1"
    company_url = "test_firm_url_1"
    location = "test_location_1"
    description = "Foo bar"
    owner = create_random_owner(db=db_session)
    job_schema = JobCreate(title=title, company=company, company_url=company_url, location=location, description=description)
    job = create_new_job(job=job_schema, db=db_session, owner_id=owner.id)
    retrieved_job = retrieve_job(id=job.id, db=db_session)
    assert retrieved_job.id == job.id
    assert retrieved_job.title == "test_title_1"
