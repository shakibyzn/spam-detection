import wandb
import wandb_workspaces.reports.v2 as wr
import wandb_workspaces.workspaces as ws
import os

def get_url(new_run_id: str) -> str:
    api = wandb.Api()

    # Fetch the project
    project = f"{os.environ['WANDB_ENTITY']}/{os.environ['WANDB_PROJECT']}"

    # Fetch all runs for the project
    runs = api.runs(project)

    baseline_run_id = None
    for run in runs:
    # Check if 'baseline' tag is present
        if 'baseline' in run.tags:
            baseline_id = run.id
    
    workspace = ws.Workspace(
        name="Compare Runs",
        entity=os.environ['WANDB_ENTITY'],
        project=os.environ['WANDB_PROJECT'],
        sections=[
            ws.Section(
                name="Test Metrics Comparison",
                panels=[
                    wr.RunComparer(diff_only='split', layout={'h': 15, 'w':24})
                ],
                is_open=True,
            ),
        ],
        runset_settings=ws.RunsetSettings(
            # Filter to include only the specified run IDs
            filters=[
                ws.Metric("ID").isin([baseline_run_id, new_run_id])
            ]
        ),
    )

    workspace.save()    

    return workspace.url
