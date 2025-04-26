# DB設計書

## 目次
1. [tasks](#tasks)
2. [schedule](#schedule)

---

## tasks

| 項番 | PK | FK | カラム名        | 項目名     | データ型         | 備考         | 初期値  | NOT NULL | 列制約         |
|----|----|----|-------------|---------|--------------|------------|------|----------|-------------|
| 1  | ●  |    | id          | タスクID 　 | INT          | 自動採番       |      | ●        | PRIMARY KEY |
| 2  |    |    | title       | タスク名    | VARCHAR(50)  |            |      | ●        |             |
| 3  |    |    | description | 説明（任意）  | VARCHAR(200) |            |      |          |             |          |
| 4  |    |    | due_date    | 期限      | DATE         | YYYY-MM-DD |      | ●        |
| 5  |    |    | status      | 進捗状況    | VARCHAR(10)  | 進捗状況（選択肢）  | todo | ●        |
| 6  |    |    | created_at  | 作成日時    | DATETIME     |            | 自動設定 | ●        |             |
| 7  |    |    | updated_at  | 更新日時    | DATETIME     |            | 自動更新 | ●        |             |

### 備考
- `status`の選択肢は以下の通り:
    - `todo`：未着手
    - `doing`:進行中
    - `done`:完了

---

## schedule
| 項番 | PK | FK | カラム名       | 項目名      | データ型        | 備考         | 初期値  | NOT NULL | 列制約         |
|----|----|----|------------|----------|-------------|------------|------|----------|-------------|
| 1  | ●  |    | id         | スケジュールID | INT         | 自動採番       | AUTO | ●        | PRIMARY KEY |
| 2  |    |    | title      | スケジュール名  | VARCHAR(50) |            |      | ●        |             |
| 3  |    |    | date       | 日付       | DATE        |            |      | ●        |             |
| 4  |    |    | time       | 時間       | TIME        |            |      | ●        |             |
| 5  |    |    | memo       | メモ       | TEXT        | タスク内容の補足   |      |          |             |
| 6  |    | ●  | task_id    | タスクID    | INT         | 実施するタスクのID |      | ●        | Ont to One  |
| 7  |    |    | created_at | 作成日時     | DATETIME    |            | 自動設定 | ●        |             |
| 8  |    |    | updated_at | 更新日時     | DATETIME    |            | 自動更新 | ●        |             |