import kubernetes.client
from kubernetes import client, config
from kubernetes.client.exceptions import ApiException
from kubernetes.client.rest import ApiException
configuration = kubernetes.client.Configuration()
from kubernetes import client, config, utils
from kubernetes.client import configuration
from kubernetes.config import ConfigException

def connection():
    config.load_kube_config()
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

def create_crd(kind: str):
    build_body = client.V1CustomResourceDefinition(api_version='shipwright.io/v1alpha1',
    kind='Build',
    metadata=client.V1ObjectMeta(name='buildpack-nodejs-build'),
    spec={"source":{
        "url":"https://github.com/shipwright-io/sample-nodejs",
        "contextDir": "source-build"},
        "strategy":{
            "name": "buildpacks-v3",
            "kind": "ClusterBuildStrategy"
            },
            "output":{
            "image": "quay.io/sunnyconcise/sample-nodejs:latest",
            "credentials": {"name": "test-pull-secret"}
            }
            })
    buildrun_body = client.V1CustomResourceDefinition(api_version='shipwright.io/v1alpha1',
    kind='BuildRun',
    metadata=client.V1ObjectMeta(generate_name='buildpack-nodejs-buildrun-'),
    spec={"buildRef":{
        "name":"buildpack-nodejs-build"}
        })
    custobjapi = client.CustomObjectsApi()
    if kind == 'Build':
        custobjapi.create_namespaced_custom_object(group='shipwright.io', version='v1alpha1', namespace='default', plural='build', body=build_body)
        return 200
    else:
        custobjapi.create_namespaced_custom_object(group='shipwright.io', version='v1alpha1', namespace='default', plural='buildrun', body=buildrun_body)
        return 200
# if __name__ == __main__:
#     main()
connection()
response = create_crd("Build")
print(response,'for build')
response = create_crd("BuildRun")
print(response,'for buildRun')
    # @then(u'Submit the BuildRun with buildRef "buildpack-nodej