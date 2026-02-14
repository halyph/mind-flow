# Languages popularity by SDKs
<!-- tags: python, java, golang, ruby, javascript -->

Unpopular opinion: measure language popularity by their usage in SDKs.
Here I've collected some random SDKs (see below) and expectedly the following languages are the top:

- Java
- Python
- JavaScript (Web and Node.js)
- C#/.NET

Less popular are:

- Go
- PHP
- C++

What surprised me it's the investment in **Rust** and some still support **Ruby**.

## Cloud

| #             | [AWS] | [Azure] | [GCP] | [IBM] |
| ------------- | ----- | ------- | ----- | --- |
| .NET          | ✅     | ✅      | ✅     |     |
| C++           | ✅     | ✅      | ✅     |     |
| Go            | ✅     | ✅      | ✅     | ✅   |
| Python        | ✅     | ✅      | ✅     | ✅   |
| Java          | ✅     | ✅      | ✅     | ✅   |
| Kotlin        | ✅     |         |       |     |
| JavaScript    | ✅     |         |       |     |
| Node.js       | ✅     |         | ✅     | ✅   |
| PHP           | ✅     |         | ✅     |     |
| Ruby          | ✅     |         | ✅     |     |
| Rust          | ✅     |         |       |     |
| Swift/iOS     | ✅     | ✅      |       | ✅   |
| SAP ABAP      | ✅     |         | ✅     |     |
| Embedded C    |        | ✅       |       |     |
| Android       |        | ✅       |       | ✅   |

## Payment

| #       | [Paypal] | [Stripe] | [Square] |
| ------- | -------- | -------- | ------ |
| .NET    | ✅        | ✅        | ✅      |
| Go      |          | ✅        |        |
| Python  | ✅        | ✅        | ✅      |
| Java    | ✅        | ✅        | ✅      |
| Node.js | ✅        | ✅        | ✅      |
| PHP     | ✅        | ✅        |        |
| Ruby    | ✅        | ✅        | ✅      |

## Random SDKs

| #             | [OpenTelemetry] | [Cloudflare] | [OpenAI] | [Splunk] | [Slack] | [Twilio] |
| ------------- | --------------- | ------------ | ------ | ------ | ----- | ------ |
| .NET          | ✅               |              | ✅      | ✅      |       | ✅      |
| C++           | ✅               |              |        |        |       |        |
| Go            | ✅               | ✅            |        |        |       | ✅      |
| Python        | ✅               | ✅            | ✅      | ✅      | ✅     | ✅      |
| Java          | ✅               |              |        | ✅      | ✅     | ✅      |
| TypeScript    |                 | ✅            |        |        |       |        |
| JavaScript    | ✅               |              |        | ✅      |       | ✅      |
| Node.js       |                 |              | ✅      |        | ✅     | ✅      |
| PHP           | ✅               |              |        |        |       | ✅      |
| Ruby          | ✅               |              |        |        |       | ✅      |
| Rust          | ✅               |              |        |        |       |        |
| Swift/iOS     | ✅               |              |        |        |       | ✅      |
| Android       |                 |              |        |        |       | ✅      |
| Erlang/Elixir | ✅               |              |        |        |       |        |


[AWS]: https://aws.amazon.com/developer/tools/
[Azure]: https://azure.github.io/azure-sdk/
[GCP]: https://cloud.google.com/sdk
[Paypal]: https://developer.paypal.com/studio/checkout/standard/integrate
[Stripe]: https://docs.stripe.com/sdks
[OpenTelemetry]: https://opentelemetry.io/status/
[IBM]: https://github.com/IBM/ibm-cloud-sdk-common
[Cloudflare]: https://developers.cloudflare.com/fundamentals/api/reference/sdks/
[OpenAI]: https://platform.openai.com/docs/libraries
[Splunk]: https://dev.splunk.com/enterprise/docs/devtools/
[Square]: https://developer.squareup.com/docs/sdks
[Slack]: https://tools.slack.dev
[Twilio]:  https://www.twilio.com/docs/libraries
