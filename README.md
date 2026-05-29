# TwiUSD Dataset

**TwiUSD** (Twitter User Stance Detection) is a user-level stance detection dataset collected from Twitter, covering two major US political targets: **Joe Biden** and **Donald Trump**.

## Dataset Overview

| Target | Split | Samples |
|--------|-------|---------|
| Biden  | Train | 6,448   |
| Biden  | Valid | 1,741   |
| Biden  | Test  | 1,773   |
| Trump  | Train | 8,120   |
| Trump  | Valid | 2,154   |
| Trump  | Test  | 2,105   |
| **Total** | — | **22,341** |

## Data Format

Each CSV file contains the following columns:

| Column | Description |
|--------|-------------|
| `id` | Twitter user ID |
| `name` | Twitter display name |
| `description` | User profile bio |
| `tweets` | List of the user's tweets (stringified Python list) |
| `follow` | List of user IDs this user follows |
| `stance` | Stance label: `favor`, `against`, or `neutral` |
| `remark` | Additional annotation remark (e.g., `none`) |

### Example Row (Biden / train.csv)



## Directory Structure



## Stance Labels

- **favor**: The user's tweets and profile indicate support for the target.
- **against**: The user's tweets and profile indicate opposition to the target.
- **neutral**: The user's stance toward the target is neutral or unclear.

## Task Description

TwiUSD supports the **user-level stance detection** task: given a user's profile description, tweet history, and social network features, predict their stance toward a political target (Biden or Trump).

This differs from post-level stance detection in that:
1. **Multiple tweets per user** — the model must aggregate evidence across a user's tweet history.
2. **User profile signals** — the bio description provides additional context.
3. **Social graph signals** — the follower list captures indirect stance signals.

## Citation

If you use this dataset in your research, please cite the original paper:



## License

Please use this dataset for academic research purposes only.
