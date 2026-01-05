# Voice Design Guide (Voice Design README)

## Overview

This guide provides instructions for creating high-quality **voice descriptions (voice_prompt)** to generate voices that meet specific requirements. The voice description serves as the blueprint for voice design and directly determines the quality of the generated voice.

---

## Technical Constraints

| Item                    | Description                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------- |
| **Length Limit**        | Each voice_prompt ≤ 200 characters                                                                |
| **Supported Languages** | Chinese only. English is not supported in the current version and will be added in future updates |

---

## Five Core Principles

### 1️⃣ Be Specific, Not Vague

**✅ Recommended**: Use perceptible and concrete voice attributes

* Pitch: low, high, bright, rich
* Speaking rate: fast, slow, rapid, steady
* Timbre: magnetic, husky, smooth, clear

**❌ Avoid**:
“Nice”, “normal”, “good” (too subjective and uninformative)

---

### 2️⃣ Multi-Dimensional, Not Single-Attribute

**✅ Recommended**: Combine at least 3–4 dimensions to create a vivid voice profile

* Persona (usage scenario) + gender + age + pitch + speaking rate + volume + timbre + emotion

**❌ Avoid**:
Only “female voice” or only “low-pitched” (too generic, lacks distinctiveness)

---

### 3️⃣ Objective, Not Subjective

**✅ Recommended**: Describe physical and acoustic characteristics

* “Slightly high-pitched with energetic delivery”
* “Slow speaking rate with clear articulation”

**❌ Avoid**:
“My favorite voice”, “This voice sounds great”

---

### 4️⃣ Original, Not Imitative

**⚠️ Copyright Notice**: Descriptions such as “sounds like XX celebrity” or “imitates XX actor” are prohibited
**✅ Recommended**: Describe voice characteristics directly rather than referencing specific individuals

---

### 5️⃣ Concise, Not Redundant

**✅ Recommended**: Ensure every word conveys meaningful information
**❌ Avoid**:
“Very, very good voice”, “Extremely, extremely gentle”

---

## Reference Dimensions for Voice Description

Based on high-quality examples, we recommend composing voice prompts using the following dimensions:

| Dimension                    | Example Options                                                                                   |
| ---------------------------- | ------------------------------------------------------------------------------------------------- |
| **Persona (Usage Scenario)** | News broadcasting, advertising voice-over, audiobooks, animated characters, documentary narration |
| **Gender**                   | Male, Female                                                                                      |
| **Age**                      | Child (~8 years), Young adult (20–30), Middle-aged (40–50), Elderly                               |
| **Personality Traits**       | Lively, calm, gentle, intellectual, cute, serious                                                 |
| **Speaking Rate & Rhythm**   | Fast, slow, moderate, urgent, steady                                                              |
| **Intonation Style**         | Rising, neutral, passionate, relaxed                                                              |
| **Timbre**                   | Deep and magnetic, crisp and bright, husky and warm, youthful                                     |

---

## High-Quality Examples

### ✅ Recommended Templates

**Example 1: Poetry Recitation**

> “A male modern poetry reciter with a deep, magnetic low voice, delivering poetry with strong rhythmic pauses, powerful volume, and intense emotional expression.”

**Example 2: News Style**

> “A female news anchor speaking standard Mandarin with a clear and bright mid-to-high pitch, steady professional pacing, strong volume, and a neutral, objective tone.”

**Example 3: Advertising Voice-Over**

> “A male voice for liquor brand advertising, featuring a rich and weathered timbre, slow and bold speaking rate, strong volume, conveying a sense of history and masculinity.”

---

## Common Mistakes and Improvements

| Type                      | ❌ Not Recommended          | ✅ Improved Version                                                           |
| ------------------------- | -------------------------- | ---------------------------------------------------------------------------- |
| **Too Generic**           | “Female voice, nice”       | “Young female voice with a clear pitch and moderate speaking rate”           |
| **Subjective Evaluation** | “A great-sounding voice”   | “Bright timbre with strong expressiveness”                                   |
| **Single Dimension**      | “Low-pitched male voice”   | “Middle-aged male with a low pitch, slow pacing, suitable for documentaries” |
| **Redundant Wording**     | “Very, very gentle voice”  | “Gentle and intellectual female voice”                                       |
| **Imitation Request**     | “Sounds like XX celebrity” | **Prohibited** — describe objective voice traits instead                     |

---

## Quick Checklist

Before submitting a voice_prompt, make sure that:

* [ ] Length ≤ 200 characters
* [ ] At least 3 different descriptive dimensions are included
* [ ] No subjective evaluation words (e.g., “nice”, “great”, “favorite”)
* [ ] No references to real individuals or imitation requests
* [ ] No repetitive or exaggerated wording
* [ ] Usage scenario is clearly defined
* [ ] All descriptors are perceptible and concrete

---
