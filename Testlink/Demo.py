
import testlink

url = 'http://10.202.228.30:8081/lib/api/xmlrpc/v1/xmlrpc.php'  # testlink服务器的api地址，只需要修改IP部分

key = '5071cda24ed90d75020320fcfd1252b5'

PROJECTNAME = '运维产品'

tlc = testlink.TestlinkAPIClient(url, key)


def get_information_test_project():
    print("Number of Projects      in TestLink: %s " % tlc.countProjects())
    print("Number of Platforms  (in TestPlans): %s " % tlc.countPlatforms())
    print("Number of Builds                   : %s " % tlc.countBuilds())
    print("Number of TestPlans                : %s " % tlc.countTestPlans())
    print("Number of TestSuites               : %s " % tlc.countTestSuites())
    print("Number of TestCases (in TestSuites): %s " % tlc.countTestCasesTS())
    print("Number of TestCases (in TestPlans) : %s " % tlc.countTestCasesTP())
    tlc.listProjects()

def get_test_suite():
    projects = tlc.getProjects()
    top_suites = tlc.getFirstLevelTestSuitesForTestProject(projects[0]["id"])
    for suite in top_suites:
        print(suite["id"], suite["name"])


# 获得项目Id和Name
for project in tlc.getProjects():
    print('projectID:{}, projectName:{}'.format(project['id'],project['name']))

print('========================')
for testsuite in tlc.getFirstLevelTestSuitesForTestProject(1):
    print('testsuiteId:{}, testsuiteName:{}'.format(testsuite['id'],testsuite['name']))
    subTestsuite = tlc.getTestSuitesForTestSuite(testsuite['id'])
    if isinstance(subTestsuite, dict):
        print(list(subTestsuite.keys()))
    else:
        print('not subTestsuite')

#tlc.createTestSuite(testprojectid= 1, testsuitename= 'API测试集子集', details= 'API测试子集描述',parentid= "3044")
tlc.createTestCase()
