import json


def test_create_job(client, normal_user_token_headers):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    response = client.post("/jobs/create-job/", data=json.dumps(data), headers=normal_user_token_headers)
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
