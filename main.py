"""
尝试使用Kimi LLM作为自己的语言模型来完成翻译功能
"""

import os

from openai import OpenAI

english_to_chinese_prompt = """
你是一个翻译大师。你同时精通中文和英文，可以帮助用户翻译在两种语言中互相转换。你会为用户提供安全，有帮助，准确的回答。如果下面的内容翻译成另一种语言。
如果用户提供中文，你会将其翻译成英文。如果用户提供英文，你会将其翻译成中文。

请注意语言的流畅性和准确性。不要直译，而是根据上下文进行翻译。如果有多种翻译方式，请选择最合适的翻译方式。
"""

source_content = """
In the early 1990s, as a young technology journalist in the Netherlands, I visited Silicon Valley. There, surprisingly, at a conference
in San Jose was where I first encountered ASML, a Dutch company
that was embroiled in a technology race with the then-unassailable
giants Canon and Nikon.
As a student and fledgling journalist in the land of Philips, I’d
never heard anything but complaints about the Japanese and the
Koreans and the disruptive effect their unfair methods were having. But in the Fairmont Hotel in San Jose, my countrymen told
me a different story. Whatever else happened, they were going to
crush their Asian competitors.
It surprised and delighted me that a machinery manufacturer
from a small town in the Dutch deep south was playing such a crucial role in information technology. After that first meeting in the
US, I kept a close watch on the engineers in Veldhoven. ASML intrigued me: a small high-tech player from my own homeland was
determining the pace of the computer chip industry. What’s more,
the company oozed enthusiasm.
It must have been somewhere around the turn of the century
that I began to play with the idea of writing a book about ASML’s
genesis. It seemed like a fascinating endeavor to lay bare the roots
of a Dutch fighting machine that had just beaten the Japanese
heavyweights Canon and Nikon.
How can a tiny company succeed where a colossus like Philips
threw in the towel? True, after 1984 it took ASML another seventeen years to grow (seemingly from nothing) into the market’s
unrivaled leader, but it was a success story to die for. I often wondered: who was behind it, and how had they pulled it off?
Yet for years the project sat in cold storage. The dot-com crisis
dealt a heavy blow to my company, Techwatch. I’d founded it in
1999 to publish my own magazine, Bits&Chips. Hit by the severe
recession, my bank account was constantly overdrawn in 2002 and
2003, and my three employees and I had to pull out all the stops
to keep the place afloat—and what’s more, I had to write the lion’s
share of my magazine myself.
Despite all that, in 2003 I visited Wim Hendriksen for a first interview for the ASML book. Wim was part of the first wave of employees who came on board shortly after the joint venture’s founding in 1984. He kept repeating one claim: “ASML as it is today—it
was planned that way from the start.” The company’s current culture, its frank, confrontational style of communication, its reckless—“all or nothing”—quest to dominate the market, the revolutionary idea to farm everything out: the seeds were all planted in
the earliest days of ASML’s existence.
Every self-respecting journalist takes a claim like that with a
hefty grain of salt. Can you conceive the culture and essence of a
company that makes extremely complex products in the space of
a few months—when the preceding years were a shambles? Can it
be true that in the spring and summer of 1984 a culture was sown
that would still exist thirty years later? I found it hard to believe.
It’s the nature of human memory to distort the past, and by then
I’d gained enough experience to know how differently different
people can view the same events.
The death of ASML’s former CEO Willem Maris at the end of 2010
was the push I needed to seriously commit to this project. I decided
to publish a Bits&Chips special issue on ASML and interviewed several insiders for it. One thing became abundantly clear: ASML’s history is anything but a straight and neatly paved road. On its way to
the top, the technology company has gone through some very deep
valleys. And many of the stories and anecdotes making the rounds
in the Netherlands’ high-tech circles turned out to be quite different
in reality. I discovered that the company’s history was riddled from
start to finish with the bizarrest of turns. In short: ASML was such
a thrilling story that I couldn’t leave it untold.
"""


def translate():
    client = OpenAI(
        api_key=os.getenv("MOONSHOT_API_KEY", ""),
        base_url="https://api.moonshot.cn/v1",
    )

    response = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {
                "role": "system",
                "content": english_to_chinese_prompt,
            },
            {
                "role": "user",
                "content": source_content
            },
        ],
        temperature=0.3,
        stream=False,
    )

    return response.choices[0].message.content


print(translate())
