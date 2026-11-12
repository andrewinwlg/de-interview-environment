from src.session import create_local_session

def test_snowpark_local_mode():
    session = create_local_session()
    try:
        rows = session.create_dataframe([[1, "ready"]], schema=["ID", "STATUS"]).collect()
        assert rows[0]["ID"] == 1
        assert rows[0]["STATUS"] == "ready"
    finally:
        session.close()
