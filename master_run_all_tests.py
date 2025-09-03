import  pytest
if __name__ == "__main__":
    # Runs all tests in the 'tests' folder
    import logging
    import os

    # Ensure logs directory exists
    os.makedirs('logs', exist_ok=True)

    # Configure logging to use logs folder
    logging.basicConfig(
        filename=os.path.join('logs', 'test_run.log'),  # Log file path
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    logging.info("Starting test run...")
    result = pytest.main(["tests/", "-v", "--html=reports/all_tests_report.html", "--self-contained-html"])
    logging.info(f"Test run completed with exit code: {result}")
    