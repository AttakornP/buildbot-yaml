from buildbot.changes.gitpoller import GitPoller
from buildbot.changes import filter
from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.schedulers.forcesched import ForceScheduler
from buildbot_config.settings import GIT, RELATION


GITPOLLERS= []
SCHEDULERS = []

for REPOSITORY_URL in GIT:
    PROJECT_NAME = REPOSITORY_URL["repository"].split("/")[1].split(".git")[0]
    BRANCH = REPOSITORY_URL["branch"]
    builder_names = RELATION[PROJECT_NAME]
    
    GITPOLLERS.append(GitPoller(
            REPOSITORY_URL["repository"], 
            project=PROJECT_NAME, 
            branch=BRANCH, 
            pollinterval=30
        )
    )
    change_filter = filter.ChangeFilter(project=PROJECT_NAME, branch=BRANCH)
    SCHEDULERS.append(SingleBranchScheduler(
            name="%s-%s-change" % (PROJECT_NAME, BRANCH), 
            change_filter = change_filter, 
            treeStableTimer=30, 
            builderNames=builder_names
        )
    )
    SCHEDULERS.append(ForceScheduler(
            name="force-%s" % PROJECT_NAME, 
            builderNames=builder_names
        )
    )

