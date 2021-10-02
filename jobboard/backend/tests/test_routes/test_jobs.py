import json


def test_create_job(client):
    data = {
        "title": "test_job",
        "company": "test_company",
        "company_url": "test_firm.com",
        "location": "test_location",
        "description": "test description",
        "date_posted": "2021-12-07",
    }
    response = client.post("/jobs/create-job", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["company"] == "test_company"


def test_retrieve_job_by_id(client):
    data = {
        "title": "test_job",
        "company": "test_company",
        "company_url": "test_firm.com",
        "location": "test_location",
        "description": "test description",
        "date_posted": "2021-12-07",
    }
    client.post("/jobs/create-job", json.dumps(data))
    response = client.get("/jobs/get/1")
    assert response.status_code == 200
    print(response)
    assert response.json()["title"] == "test_job"
