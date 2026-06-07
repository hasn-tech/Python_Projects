from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "start_date": datetime(2024, 1, 1)
}

with DAG(
    dag_id="emr_pyspark_bash_operator",
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args
) as dag:

    submit_emr_step = BashOperator(
        task_id="submit_emr_pyspark_job",
        bash_command="""
        aws emr add-steps \
            --cluster-id j-XXXXXXXXXXXXX \
            --steps Type=Spark,Name="PySparkJob",ActionOnFailure=CONTINUE,\
Args=[\
s3://my-bucket/scripts/emr_etl.py,\
--deploy-mode,cluster,\
--master,yarn]
        """
    )

    submit_emr_step