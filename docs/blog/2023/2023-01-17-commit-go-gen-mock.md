# Golang: Do you commit your generated mocks to repo?
> | golang |

I've discovered that there is no consensus about "*Committing generate mocks to the repo*". That's why I've looked around and found some discussions, pros&cons (see [References](#references)).

Also there is interesting statement in the official Golang article [About the go command](https://go.dev/doc/articles/go_command):

> As mentioned above, the go command is not a general-purpose build tool. In particular, it does not have any facility for generating Go source files during a build, although it does provide go generate, which can automate the creation of Go files before the build. For more advanced build setups, you may need to write a makefile (or a configuration file for the build tool of your choice) to **run whatever tool creates the Go files and then check those generated source files into your repository. This is more work for you, the package author, but it is significantly less work for your users, who can use "go get" without needing to obtain and build any additional tools.**

So actually they are suggesting always committing generated code.

I made a conclusion for myself: **you should commit generated mocks to the repo!**

## References

- [Comparison of golang mocking libraries](https://gist.github.com/maratori/8772fe158ff705ca543a0620863977c2)
- [GoMock vs. Testify: Mocking frameworks for Go](https://blog.codecentric.de/gomock-vs-testify)
- [Reddit: What mocking framework do you prefer?](https://www.reddit.com/r/golang/comments/qe4a1c/what_mocking_framework_do_you_prefer/)
- [Reddit: Do you commit all the generated code in your Golang applications?](https://www.reddit.com/r/golang/comments/8mbi47/do_you_commit_all_the_generated_code_in_your/)
- [Reddit: Do you commit your mocks to repo?](https://www.reddit.com/r/golang/comments/c1ylf8/do_you_commit_your_mocks_to_repo/)
- [SO: Should a developer commit Go generated code?](https://stackoverflow.com/questions/56415527/should-a-developer-commit-go-generated-code)
- [Should I commit generated Go code?](https://www.jvt.me/posts/2022/05/05/commit-go-generate/)
- [Standard Package Layout](https://www.gobeyond.dev/standard-package-layout/)

The popularity of Golang mock libraries:

- [golang/mock](https://github.com/golang/mock) ⭐ 8.5k 
- [vektra/mockery](https://github.com/vektra/mockery) ⭐ 4.4k
- [minimock](https://github.com/gojuno/minimock) ⭐ 480
- [moq](https://github.com/matryer/moq) ⭐ 1.5k

# Sample of popular repos with committed mocks

I have decided to check some public repos and whether they are committing generated mocks.

Based on libraries popularity I will concentrate on **golang/mock** and **vektra/mockery** only (see report below).

## Hashicorp

| **Repo**| **Comments or Samples** |
| -- | -- |
| [waypoint](https://github.com/hashicorp/waypoint) ⭐ 4.7k | <span style="background-color:#ffe090;color:#352917">**vektra/mockery**</span> [is_auth_method__method.go](https://github.com/hashicorp/waypoint/blob/0184c43445d27a027bcfa7e55c9d5668e5598dd6/pkg/server/gen/mocks/is_auth_method__method.go) |
| [terraform](https://github.com/hashicorp/terraform) ⭐ 36.2k  | <span style="background-color:#ccebaf;color:#09643c">**golang/mock**</span> [mock_proto/mock.go](https://github.com/hashicorp/terraform/blob/d35bc0531255b496beb5d932f185cbcdb2d61a99/internal/plugin6/mock_proto/mock.go)|
| [consul-terraform-sync](https://github.com/hashicorp/consul-terraform-sync) ⭐ 110 | <span style="background-color:#ffe090;color:#352917">**vektra/mockery**</span> [terraformExec.go](https://github.com/hashicorp/consul-terraform-sync/blob/40ec791893fec56ea1c57d1e7f3fbdeb467d1775/mocks/client/terraformExec.go)|
| [consul](https://github.com/hashicorp/consul) ⭐ 26.1k | <span style="background-color:#dfc2ef;color:#451d71">**manually implemented**</span> [mock_api_test.go](https://github.com/hashicorp/consul/blob/bf0f61a87884d444d472b981099163856658d3ea/api/mock_api_test.go) <br /> <span style="background-color:#ffe090;color:#352917">**vektra/mockery**</span> [mock_Login.go](https://github.com/hashicorp/consul/blob/02cff2394d921aeaecaf043fe1b1d519f465c3e6/agent/grpc-external/services/acl/mock_Login.go) |

## Uber

| **Repo**| **Comments or Samples** |
| -- | -- |
| [cadence](https://github.com/uber/cadence) ⭐ 6.7k | <span style="background-color:#ccebaf;color:#09643c">**golang/mock**</span> [authority_mock.go](https://github.com/uber/cadence/blob/9f219005095082151ef051826358f7f98e191a67/common/authorization/authority_mock.go), [cadence/search?q=MockGen](https://github.com/uber/cadence/search?q=MockGen>) |
| [aresdb](https://github.com/uber/aresdb) ⭐ 2.9k | <span style="background-color:#ffe090;color:#352917">**vektra/mockery**</span> [PeerDataNode_BenchmarkFileTransferClient.go](https://github.com/uber/aresdb/blob/a8d2aedc6850b10a6cc9381ba780800290b2756d/datanode/generated/proto/rpc/mocks/PeerDataNode_BenchmarkFileTransferClient.go) |

## Dropbox

| **Repo**| **Comments or Samples** |
| -- | -- |
| [kglb](https://github.com/dropbox/kglb) ⭐ 131 | <span style="background-color:#dfc2ef;color:#451d71">**manually implemented**</span> [mock_modules.go](https://github.com/dropbox/kglb/blob/7f86d1804d5d14527665302545ef2da2dffed778/kglb/data_plane/mock_modules.go) |
| [dropbox/godropbox](https://github.com/dropbox/godropbox) ⭐ 4.1k | <span style="background-color:#dfc2ef;color:#451d71">**manually implemented**</span> [mock_client_test.go](https://github.com/dropbox/godropbox/blob/52ad444d35023d078d496d305d75511e772f0295/memcache/mock_client_test.go)|

## Gitlab

| **Repo**| **Comments or Samples** |
| -- | -- |
| [gitlab-runner](https://gitlab.com/gitlab-org/gitlab-runner) ⭐ 2.1k | <span style="background-color:#ffe090;color:#352917">**vektra/mockery**</span> [mock_requester.go](https://gitlab.com/gitlab-org/gitlab-runner/-/blob/main/network/mock_requester.go) |
| [fargate](https://gitlab.com/gitlab-org/ci-cd/custom-executor-drivers/fargate) ⭐ 40 | <span style="background-color:#ffe090;color:#352917">**vektra/mockery**</span> [mock_ec2Client.go](https://gitlab.com/gitlab-org/ci-cd/custom-executor-drivers/fargate/-/blob/master/aws/mock_ec2Client.go) |

## Other

| **Repo**| **Comments or Samples** |
| -- | -- |
| [jaegertracing/jaeger](https://github.com/jaegertracing/jaeger) ⭐ 17.1k | <span style="background-color:#ffe090;color:#352917">**vektra/mockery**</span> [DependenciesReaderPluginServer.go](https://github.com/jaegertracing/jaeger/blob/main/proto-gen/storage_v1/mocks/DependenciesReaderPluginServer.go) |
| [ignite/cli](https://github.com/ignite/cli) ⭐ 1k | <span style="background-color:#ffe090;color:#352917">**vektra/mockery**</span> [gasometer.go](https://github.com/ignite/cli/blob/efe4c05fc5e38be48b7b89b651d9453641aba0b9/ignite/pkg/cosmosclient/mocks/gasometer.go) |
| [projectcontour/contour](https://github.com/projectcontour/contour) ⭐ 3.3k | <span style="background-color:#ffe090;color:#352917">**vektra/mockery**</span> [manager.go](https://github.com/projectcontour/contour/blob/2287c8e4dbea7ded3086e0fb300714cc482f0287/internal/controller/mocks/manager.go)|
| [tendermint/tendermint](https://github.com/tendermint/tendermint) ⭐ 5.4k   | <span style="background-color:#ffe090;color:#352917">**vektra/mockery**</span> [block_store.go](https://github.com/tendermint/tendermint/blob/64747b2b184184ecba4f4bffc54ffbcb47cfbcb0/state/mocks/block_store.go) |
| [weaveworks/eksctl](https://github.com/weaveworks/eksctl) ⭐ 4.3k           | <span style="background-color:#ffe090;color:#352917">**vektra/mockery**</span> [ConfigProvider.go](https://github.com/weaveworks/eksctl/blob/00f47703e4d8311518507d0f2dff42b59fb3c465/pkg/eks/mocks/ConfigProvider.go) |
| [google/skia-buildbot](https://github.com/google/skia-buildbot) ⭐ 119      | <span style="background-color:#ffe090;color:#352917">**vektra/mockery**</span>  [DataFrameBuilder.go](https://github.com/google/skia-buildbot/blob/4c87209ff9378a9befc65d5f93c4040d4fdd5922/perf/go/dataframe/mocks/DataFrameBuilder.go) |