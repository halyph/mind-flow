# Lightbend is Changing the License for Akka
<!-- tags: scala, akka -->

## References

- Original Lightbend blog post [Why We Are Changing the License for Akka](https://www.lightbend.com/blog/why-we-are-changing-the-license-for-akka)
- PR [Change license #31561](https://github.com/akka/akka/pull/31561)
- Discuss [2.6.x maintenance proposal](https://discuss.lightbend.com/t/2-6-x-maintenance-proposal/9949) - Lightbend will be addressing critical security updates and critical bugs in Akka v2.6.x under the current Apache 2 license until September 2023
- Community reaction:
  - [Hacker News](https://news.ycombinator.com/item?id=32746807)
  - Reddit [1](https://www.reddit.com/r/scala/comments/x7xyzr/why_we_are_changing_the_license_for_akka/) and [2](https://www.reddit.com/r/scala/comments/x7yr9b/akka_is_moving_away_from_open_source/)

## My thoughts

*TL;DR* Lightbend decided to change Akka license from Apache 2.0 to Business Source License (BSL) v1.1.

> The BSL is a “Source Available” license that freely allows using the code for development and other non-production work such as testing. Production use of the software requires a commercial license from Lightbend. The commercial license will be available at no charge for early-stage companies (less than US $25 million in annual revenue). By enabling early-stage companies to use Akka in production for free, we hope to continue to foster the innovation synonymous with the startup adoption of Akka.

It was announced 2 days ago (September 7, 2022), I expected a shit-storm and decided to wait and read comments (see links above).

I have nothing against Lightbend's decision.

I used **Akka-http**, **Akka-Streams** and **Play Framework**. I like Akka-http for it's simplicity. Life is unpredictable and we all must adjust our plans.

I will not recommend my team or my current and future employer to use Akka. There are several other libraries and frameworks which can replace Akka.

I see the following alternatives for Scala: [Typelevel](https://typelevel.org/projects/) stack or [ZIO](https://zio.dev). One downside of *ZIO* it's his opinionated approach.
For now, I have decided to check *Typelevel* stack.

But, in case of failure on Scala front, I have Java backup - **Spring Boot** and *Co*. People are saying that Java 18 is cool.

## Historical Notes

I forgot to mention that Lightbend has stopped [Lagom](https://www.lagomframework.com) active development and made [Playframework](https://www.playframework.com) community-led project.

Read more here:

- [On the future of Play Framework](https://www.lightbend.com/blog/on-the-future-of-play-framework) - October 2021
- [The future of Lagom](https://discuss.lightbend.com/t/the-future-of-lagom/8962) - October 2021
