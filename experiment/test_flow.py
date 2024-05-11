import mlflow

with mlflow.start_run(run_name='ParentRun') as parent_run:
    # Log parameters or tags to the parent run
    mlflow.log_param('param1', 'value1')

    # Start a nested child run
    with mlflow.start_run(run_name='ChildRun', nested=True) as child_run:
        # Log metrics or artifacts to the child run
        mlflow.log_metric('metric1', 0.87)