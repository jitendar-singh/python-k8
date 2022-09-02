from kubernetes import client, config
from kubernetes.client import configuration
from kubernetes.config import ConfigException
from kubernetes.client.rest import ApiException


def main():
    config.load_kube_config()
    configuration = kubernetes.client.Configuration()
    try:
        config.load_incluster_config()
    except config.ConfigException:
        try:
            config.load_kube_config()
            print("Logged into cluster")
        except config.ConfigException:
            logging.critical("This is CRITICAL")
            raise Exception("Cluster probe failed")
    print("Active host is %s" % configuration.Configuration().host)

if __name__ == '__main__':
    main()












#     deployment_body = create_deployment_object()
#     appsv1 = client.AppsV1Api()
#     deploy = appsv1.create_namespaced_deployment(namespace='registry',body= deployment_body)
#     print("INFO: Deployment: ",deploy.metadata.name," created")
#     svc = create_service()
#     print("INFO: Service: ",svc," created")






#     v1 = client.CoreV1Api()
#     ns_body = client.V1Namespace(
#         api_version="v1",
#         kind="Namespace",
#         metadata={
#             "name": "registry"
#         }
#     )
#     res = v1.create_namespace(ns_body)
#     registry_namespace = res.metadata.name
#     print('INFO: Namespace: ',registry_namespace,' created')

# DEPLOYMENT_NAME = "registry"


# def create_deployment_object():
#     # Configureate Pod template container
#     container = client.V1Container(
#         name="registry",
#         image="registry:2",
#         image_pull_policy="IfNotPresent",
#         env=[client.V1EnvVar(name="REGISTRY_STORAGE_DELETE_ENABLED",value="true")],
#         ports=[client.V1ContainerPort(container_port=5000,host_port=32222)],
#         resources=client.V1ResourceRequirements(
#             requests={"cpu": "100m", "memory": "128M"},
#             limits={"cpu": "100m", "memory": "128M"},
#         ),
#     )

#     # Create and configure a spec section
#     template = client.V1PodTemplateSpec(
#         metadata=client.V1ObjectMeta(labels={"app": "registry"},namespace="registry"),
#         spec=client.V1PodSpec(containers=[container]),
#     )

#     # Create the specification of deployment
#     spec = client.V1DeploymentSpec(
#         replicas=1, template=template, selector={
#             "matchLabels":
#             {"app": "registry"}})

#     # Instantiate the deployment object
#     deployment = client.V1Deployment(
#         api_version="apps/v1",
#         kind="Deployment",
#         metadata=client.V1ObjectMeta(name=DEPLOYMENT_NAME),
#         spec=spec,
#     )

#     return deployment

# def create_service():
#     v1 = client.CoreV1Api()
#     service_body = client.V1Service(
#         api_version="v1",
#         kind="Service",
#         metadata={
#             "labels":
#             {"app": "registry"},
#             "name": "registry",
#             "namespace": "registry"
#         },
#         spec= client.V1ServiceSpec(
#             ports=[client.V1ServicePort(port=32222,node_port=32222,protocol="TCP",target_port=5000)],
#             selector={"app": "registry"},
#             type="NodePort"
#         )
#     )
#     service = v1.create_namespaced_service('registry', service_body)
#     return service.metadata.name




















    # appsv1 = client.AppsV1Api()
    # deployment_body = client.V1Deployment(
    #     api_version="apps/v1",
    #     kind="Deployment",
    #     metadata={
    #         "name": "registry",
    #         "namespace": "registry"
    #     },
    #     spec=client.V1DeploymentSpec(
    #         replicas=1,
    #         selector={
    #             "matchLabels":{
    #                 "app": "registry"
    #             }
    #         },
    #         template={
    #             "metadata":{
    #                 "labels":{
    #                     "app": "registry"
    #                 }
    #             },
    #             "spec":{
    #                 "containers":[{
    #                     "image": "registry:2",
    #                     "name": "registry",
    #                     "imagePullPolicy": "IfNotPresent",
    #                     "env":{
    #                         "name": "REGISTRY_STORAGE_DELETE_ENABLED",
    #                         "value": "true"
    #                     },
    #                     "ports":{
    #                         "containerPort": 5000,
    #                         "hostPort": 32222
    #                     },
    #                     "resources":{
    #                         "requests":{
    #                             "cpu": "100m",
    #                             "memory": "128M"
    #                         },
    #                         "limits":{
    #                             "cpu": "100m",
    #                             "memory": "128M"
    #                         }
    #                     }
    #                 }
    #             ]
    #         }
    #         }
    #     )
    # )
            
            
    #         {
    #         "replicas": 1,
    #         "selector":{
    #             "matchLabels":{
    #                 "app": "registry"
    #             }
    #         },
    #         "template":{
    #             "metadata":{
    #                 "labels":{
    #                     "app": "registry"
    #                 }
    #             },
    #             "spec":{
    #                 "containers":{
    #                     "image": "registry:2",
    #                     "name": "registry",
    #                     "imagePullPolicy": "IfNotPresent",
    #                     "env":{
    #                         "name": "REGISTRY_STORAGE_DELETE_ENABLED",
    #                         "value": "true"
    #                     },
    #                     "ports":{
    #                         "containerPort": 5000,
    #                         "hostPort": 32222
    #                     },
    #                     "resources":{
    #                         "requests":{
    #                             "cpu": "100m",
    #                             "memory": "128M"
    #                         },
    #                         "limits":{
    #                             "cpu": "100m",
    #                             "memory": "128M"
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # )
    
    # spec = client.V1DeploymentSpec(
    #     replicas=1,
    #     selector=client.V1LabelSelector(
    #         match_labels={"app": "nginx"}
    #     ),
    #     template=template)
    # # Deployment
    # deployment = client.V1Deployment(
    #     api_version="apps/v1",
    #     kind="Deployment",
    #     metadata=client.V1ObjectMeta(name="deploy-nginx"),
    #     spec=spec)


    # v1 = client.CoreV1Api()
    # secret_body = client.V1Secret(api_version="v1",
    #     kind="Secret",
    #     metadata=client.V1ObjectMeta(name="test-pull-secret",namespace="default"),
    #     type="kubernetes.io/dockerconfigjson",
    #     data={".dockerconfigjson": "ewogICJhdXRocyI6IHsKICAgICJxdWF5LmlvIjogewogICAgICAiYXV0aCI6ICJjM1Z1Ym5samIyNWphWE5sT21rM05EUklSbHB6TUVKcFMwUkNiVzF6VHpoVVVEbHhNSFpQVFZkTU1HcHhTM0ZKZFZkUmJsSlhTRmxNY2pSQ1JFVTJORXR5YTNSNGVHVnFNbHBTVTJNPSIsCiAgICAgICJlbWFpbCI6ICIiCiAgICB9CiAgfQp9"})
    # v1.create_namespaced_secret('default', secret_body)
    # secret = v1.read_namespaced_secret('test-pull-secret', namespace='default')
    # print('Secret: %s' %secret.metadata.name,' created')

    # with open(path.join(path.dirname(__file__), "deployment.yaml")) as f:
    #         dep = yaml.safe_load(f)
    # k8s_client = client.ApiClient()
    # utils.create_from_yaml(k8s_client, 'deployment.yaml')
    # # print("Deployment created. status='%s'" % str(resp.status))
    # with open(path.join(path.dirname(__file__), "deployment.yaml")) as f:
    #         dep = yaml.safe_load(f)
    #         k8s_beta = client.ExtensionsV1beta1Api()
    #         resp = k8s_beta.create_namespaced_deployment(
    #         body=dep, namespace="default")
    #         print("Deployment created. status='%s'" % str(resp.status))






    # yaml_file = './deployment.yaml'
    # k8s_client = client.ApiClient()
    # utils.create_from_yaml(k8s_client, yaml_file)

    # apiextensionv1 = client.ApiextensionsV1Api()
    # crds=apiextensionv1.list_custom_resource_definition()
    # for crd in crds.items:
    #     print('%s' %crd.metadata.name)

    
    # body = client.V1CustomResourceDefinition(api_version='shipwright.io/v1alpha1',
    #    kind='Build',
    #    metadata=client.V1ObjectMeta(name='buildpack-nodejs-build'),
    #    spec={"source":{
    #     "url":"https://github.com/shipwright-io/sample-nodejs",
    #     "contextDir": "source-build"},
    #     "strategy":{
    #         "name": "buildpacks-v3",
    #         "kind": "ClusterBuildStrategy"
    #     },
    #     "output":{
    #         "image": "quay.io/sunnyconcise/sample-nodejs:latest",
    #         "credentials": {"name": "test-pull-secret"}
    #         }
    #    })
    # custobjapi = client.CustomObjectsApi()
    # custobjapi.create_namespaced_custom_object(group='shipwright.io', version='v1alpha1', namespace='default', plural='builds', body=body)
    # # res = custobjapi.get_cluster_custom_object_status(group='shipwright.io', version='v1alpha1', name='buildpack-nodejs-build', plural='builds')
    # res = custobjapi.get_namespaced_custom_object(group='shipwright.io', version='v1alpha1',namespace='default', name='buildpack-nodejs-build', plural='builds')
    # # apiextensionv1.create_custom_resource_definition(body)
    # # build = apiextensionv1.create_custom_resource_definition(body)
    
    # buildrun_body = client.V1CustomResourceDefinition(api_version='shipwright.io/v1alpha1',
    #     kind='BuildRun',
    #     metadata=client.V1ObjectMeta(generate_name='buildpack-nodejs-buildrun-'),
    #     spec={"buildRef":{
    #         "name":"buildpack-nodejs-build"}
    #     }
    # )
    # custobjapi.create_namespaced_custom_object(group='shipwright.io', version='v1alpha1', namespace='default', plural='buildruns', body=buildrun_body)






    # k8s_client = client.ApiClient()
    


    # v1 = client.CoreV1Api()
    # node_state = {}
    # node_lst = v1.list_node()
    # for nodes in node_lst.items:
    #     print(nodes.metadata.name)
    #     node_status = v1.read_node_status(nodes.metadata.name)
    #     for status in node_status.status.conditions:
    #         node_state[status.type] = status.status
    # if 'Ready' in node_state.keys():
    #     if node_state['Ready'] == 'True':
    #         print("Node ",nodes.metadata.name," is Ready")
    #     else:
    #         print(node_state['Ready'])
    #     # print(node_state)








    # v1 = client.CoreV1Api()
    # print('Listing all namespaces')
    # namespace_lst = v1.list_namespace()
    # namespaces = [item.metadata.name for item in namespace_lst.items]
    # print(namespaces)
    # appsv1 = client.AppsV1Api()
    # thread = appsv1.list_namespaced_deployment('shipwright-build')
    # deployments = [item.metadata.name for item in thread.items]
    # # print(deployments)
    # deployment_name = ' '.join(map(str, deployments))
    # print(deployment_name)
    # # dep = appsv1.read_namespaced_deployment(deployment_name, 'shipwright-build',pretty=True)
    # # dep_repset = appsv1.list_namespaced_replica_set('shipwright-build')
    # # print(dep_repset)

    # state = appsv1.read_namespaced_deployment_status(deployment_name, 'shipwright-build',pretty=True)
    # desired_replicas = state.spec.replicas
    # ready_replicas = state.status.ready_replicas
    # if desired_replicas == ready_replicas:
    #     return True
    # else:
    #     raise Exception("Deployment ",deployment," desired replicas:<",desired_replicas,"> ready replicas:<",ready_replicas,">")
		
    # print(state)
    # print(state.status.unavailable_replicas)
    # deployment_state = [item.metadata.name for item in state]
    # print(deployment_state)
    # cusobj = client.ApiextensionsV1Api()
    # res = cusobj.list_custom_resource_definition()
    # crd_scope = {}
    # for item in res.items:
    #     crds = item.metadata.name
    #     scope = item.spec.scope
    #     crd_scope[crds]=scope
    
    # res = cusobj.read_custom_resource_definition('clusterbuildstrategies.shipwright.io')
    # res1 = cusobj.list_custom_resource_definition()
    # for item in res1.items:
    #     print(item.metadata.name)
    
    # cstobj = client.CustomObjectsApi()
    # customobj = ['buildah','buildkit','buildpacks-v3','kaniko','ko','source-to-image']
    # for obj in customobj:
    #     res = cstobj.get_cluster_custom_object('shipwright.io', 'v1alpha1', 'clusterbuildstrategies', obj)
    #     if res is None:
    #         print(False)
    #     else:
    #         print(True)
    



    # result = cusobj.get_cluster_custom_object('shipwright.io', 'v1alpha1', 'buildruns', 'buildruns')
    # crd = {'buildruns.shipwright.io': 'Namespaced', 'builds.shipwright.io': 'Namespaced', 
    # 'buildstrategies.shipwright.io': 'Namespaced', 'clusterbuildstrategies.shipwright.io': 'Cluster',
    #  'clustertasks.tekton.dev': 'Namespaced', 'conditions.tekton.dev': 'Namespaced', 
    #  'pipelineresources.tekton.dev': 'Namespaced', 'pipelineruns.tekton.dev': 'Namespaced', 
    #  'pipelines.tekton.dev': 'Namespaced', 'runs.tekton.dev': 'Namespaced', 
    #  'taskruns.tekton.dev': 'Namespaced', 'tasks.tekton.dev': 'Namespaced'}
    # for x, y in crd.items():
    #     res = crd_res(x, y)
    #     print(res)
