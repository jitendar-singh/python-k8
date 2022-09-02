def crd_res(res_name, scope):
    crds = {'buildruns.shipwright.io': 'Namespaced', 'builds.shipwright.io': 'Namespaced', 
    'buildstrategies.shipwright.io': 'Namespaced', 'clusterbuildstrategies.shipwright.io': 'Cluster',
     'clustertasks.tekton.dev': 'Cluster', 'conditions.tekton.dev': 'Namespaced', 
     'pipelineresources.tekton.dev': 'Namespaced', 'pipelineruns.tekton.dev': 'Namespaced', 
     'pipelines.tekton.dev': 'Namespaced', 'runs.tekton.dev': 'Namespaced', 
     'taskruns.tekton.dev': 'Namespaced', 'tasks.tekton.dev': 'Namespaced'}

    if crds[res_name] == scope:
        return True
    else:
        return False