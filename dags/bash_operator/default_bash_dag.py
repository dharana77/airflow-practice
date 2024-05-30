from dags.default_dag import create_dag

dag = create_dag("BashOperator")

run_this = BashOperator(
    task_id='run_this_task',
    bash_command="echo bash",
    dag=dag,
)


also_run_this = BashOperator(

)