import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    num_pages = yield context.call_activity('GetCovidPages', None)
    url_tasks = [context.call_suborchestrator('GetCovidStats', i) for i in range(1, num_pages+1)]
    #url_tasks = [context.call_activity('GetCovidStats', i) for i in range(1, num_pages+1)]
    stats = yield context.task_all(url_tasks)
    persist_tasks = [context.call_activity('PersistCovidStats', r) for batch in stats for r in batch]
    result = yield context.task_all(persist_tasks)
    
main = df.Orchestrator.create(orchestrator_function)