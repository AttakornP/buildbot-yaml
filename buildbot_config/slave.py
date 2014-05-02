from buildbot.buildslave import BuildSlave
from buildbot.config import BuilderConfig
from buildbot.process.factory import BuildFactory
from buildbot.steps.shell import ShellCommand
from buildbot_config.settings import BUIDER, FACTORY 


BUILDERS= []
SLAVES = [] 

for slave in BUIDER:
    builder_name = slave["name"]
    SLAVES.append(BuildSlave(
            slave["name"], 
            slave["password"]
        )
    )
    
    factory_steps = FACTORY[builder_name]
    factory = BuildFactory()
    for step in factory_steps: 
        factory.addStep(ShellCommand(
            command=step["command"], 
            workdir=step.get("workdir", "src")
        ))

    BUILDERS.append(BuilderConfig(name=builder_name
            , slavenames=[builder_name]
            , factory=factory)
    )
