# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 18:41
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `5dc83ceb-fefb-4346-bba2-da107525e029` | unsure | 0.520 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `549b06b8-b477-4a80-833a-db69d695dddf` | unsure | 0.650 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `36e59006-c97e-4573-9e1b-e9eee6b4021d` | unsure | 0.500 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `331f0e77-decb-4c34-825d-20ad88986f53` | unsure | 0.720 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `eb359644-c933-4c4d-86fc-b28e87003fbc` | human | 0.800 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `43be7ac7-90c3-46ad-ada4-ae19317b8cc5` | unsure | 0.630 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `838a4738-5312-4632-9899-c27b8c005e5e` | unsure | 0.540 |  |
| EV08 | evasion | signal one: text below the token window | 422 | `—` | — | — |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `0bf381dc-8339-44c4-a890-da8be3c8e5a8` | unsure | 0.500 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `0169faf7-d48f-446f-8494-cbedea9fc718` | unsure | 0.770 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c928ad9e-b8c3-4f94-bbec-d295c3f51749` | unsure | 0.510 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `5fdd7de9-7b51-4d7c-ba7d-653a7484c920` | unsure | 0.780 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `55e09f68-ce07-4a02-8da8-bab55ca23ecc` | unsure | 0.730 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `02e89ced-e9b1-4460-b0f7-bf3e805ce3ee` | unsure | 0.690 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `8dc0d408-e61d-4d7c-8b8d-56df76d0427d` | unsure | 0.790 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `27f7ea48-e1a3-4ddc-8a55-662b88f6a6e9` | unsure | 0.600 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `df76e919-39c8-41d9-bdec-c3a2d8de4046` | unsure | 0.540 |  |
| FP08 | false_positive | very short genuine human submission | 422 | `—` | — | — |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `1d304647-7b27-4757-a3f9-2cb158b89282` | unsure | 0.720 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c8d4b917-6968-4ec1-8990-44c4b9d7bd6f` | human | 0.850 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `b6f4677a-2a3a-4840-bbf9-93d2aedc1e69` | unsure | 0.570 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `3166a953-1a18-429f-9c17-2bced8f01056` | unsure | 0.550 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `d9d9b1c2-d317-4a9d-a424-4ff8f1db5880` | unsure | 0.570 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `87aee3ba-d81d-4624-806c-3158d024ab49` | unsure | 0.520 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 422 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 422 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 422 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 422 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 422 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 422 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 422 | `—` | — | — |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 422 | `—` | — | — |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 422 | `—` | — | — |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 422 | `—` | — | — |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 422 | `—` | — | — |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 422 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "5dc83ceb-fefb-4346-bba2-da107525e029",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.52,
  "model_score": 0.1635,
  "style_score": 0.8667,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "549b06b8-b477-4a80-833a-db69d695dddf",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.65,
  "model_score": 0.5943,
  "style_score": 0.0998,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "36e59006-c97e-4573-9e1b-e9eee6b4021d",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.6662,
  "style_score": 0.3248,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "331f0e77-decb-4c34-825d-20ad88986f53",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.72,
  "model_score": 0.6114,
  "style_score": 0.8338,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "eb359644-c933-4c4d-86fc-b28e87003fbc",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.8,
  "model_score": 0.3212,
  "style_score": 0.0824,
  "label": "We think this was probably written by a person. Nothing in it looked like the kind of writing automated tools produce.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "43be7ac7-90c3-46ad-ada4-ae19317b8cc5",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.63,
  "model_score": 0.5727,
  "style_score": 0.1664,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "838a4738-5312-4632-9899-c27b8c005e5e",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.54,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_EV08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "0bf381dc-8339-44c4-a890-da8be3c8e5a8",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.7042,
  "style_score": 0.2911,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "0169faf7-d48f-446f-8494-cbedea9fc718",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.77,
  "model_score": 0.9792,
  "style_score": 0.5664,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "c928ad9e-b8c3-4f94-bbec-d295c3f51749",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.51,
  "model_score": 0.6175,
  "style_score": 0.399,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "5fdd7de9-7b51-4d7c-ba7d-653a7484c920",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.78,
  "model_score": 0.7387,
  "style_score": 0.8137,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "55e09f68-ce07-4a02-8da8-bab55ca23ecc",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.73,
  "model_score": 0.8051,
  "style_score": 0.6461,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "02e89ced-e9b1-4460-b0f7-bf3e805ce3ee",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.69,
  "model_score": 0.8329,
  "style_score": 0.5513,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "8dc0d408-e61d-4d7c-8b8d-56df76d0427d",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.79,
  "model_score": 0.8005,
  "style_score": 0.7744,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "27f7ea48-e1a3-4ddc-8a55-662b88f6a6e9",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.8814,
  "style_score": 0.31,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "df76e919-39c8-41d9-bdec-c3a2d8de4046",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.54,
  "model_score": 0.8816,
  "style_score": 0.1968,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_FP08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "1d304647-7b27-4757-a3f9-2cb158b89282",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.72,
  "model_score": 0.4625,
  "style_score": 0.1,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "c8d4b917-6968-4ec1-8990-44c4b9d7bd6f",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.85,
  "model_score": 0.2044,
  "style_score": 0.088,
  "label": "We think this was probably written by a person. Nothing in it looked like the kind of writing automated tools produce.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "b6f4677a-2a3a-4840-bbf9-93d2aedc1e69",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.57,
  "model_score": 0.5943,
  "style_score": 0.5363,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "3166a953-1a18-429f-9c17-2bced8f01056",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.55,
  "model_score": 0.4998,
  "style_score": 0.4033,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "d9d9b1c2-d317-4a9d-a424-4ff8f1db5880",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.57,
  "model_score": 0.6401,
  "style_score": 0.2286,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "87aee3ba-d81d-4624-806c-3158d024ab49",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.52,
  "model_score": 0.5583,
  "style_score": 0.4091,
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
