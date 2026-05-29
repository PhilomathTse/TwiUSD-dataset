# TwiUSD Dataset

**TwiUSD** (Twitter User Stance Detection) is a user-level stance detection dataset collected from Twitter, targeting two major US political figures: **Joe Biden** and **Donald Trump**.

## Dataset Statistics

| Target | Train | Valid | Test | Total |
|--------|-------|-------|------|-------|
| Biden  | 5,448 | 1,837 | 1,884 | 9,169 |
| Trump  | 5,315 | 2,268 | 2,215 | 9,798 |
| **Total** | **10,763** | **4,105** | **4,099** | **18,967** |

## Directory Structure

```
TwiUSD/
├── biden/
│   ├── train.csv
│   ├── valid.csv
│   └── test.csv
└── trump/
    ├── train.csv
    ├── valid.csv
    └── test.csv
```

## Data Format

Each CSV file contains the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `id` | int | Twitter user ID |
| `name` | str | Twitter display name |
| `description` | str | User profile bio |
| `tweets` | list | User's recent tweets (stringified Python list) |
| `follow` | list | IDs of accounts this user follows |
| `stance` | str | Stance label: `favor`, `against`, or `neutral` |
| `remark` | str | Annotation remark (e.g., `none`) |
| `followed_tweet` | str | Tweets from followed accounts (social context signal) |

### Example

```
id,name,description,tweets,follow,stance,remark,followed_tweet
2973525349,Steve Sanchez,"Provide insight...","['RT @Jim_Jordan: ...']","['2302407500']",favor,none,...
```

## Stance Labels

| Label | Description |
|-------|-------------|
| `favor` | User's content indicates support for the target |
| `against` | User's content indicates opposition to the target |
| `neutral` | User's stance is neutral or ambiguous |

## Task Description

TwiUSD supports **user-level stance detection**: given a user's profile, tweet history, and social network context, predict their stance toward a political target.

Key characteristics:
- **User-level** (not post-level): stance is inferred from an aggregation of a user's activity
- **Social context**: `followed_tweet` provides indirect stance signals from the user's social network
- **Two targets**: Biden and Trump, enabling cross-target transfer experiments

## License

For academic research use only.
