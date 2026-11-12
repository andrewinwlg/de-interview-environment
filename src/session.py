from snowflake.snowpark import Session

def create_local_session():
    return Session.builder.config("local_testing", True).create()
