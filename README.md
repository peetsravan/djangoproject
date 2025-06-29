# 📱 NextLabs – App-Download Rewards Platform

A Django 5 project where:

* **Admins** create Android-app listings and assign point values.
* **Users** sign up, browse apps, earn points by uploading screenshots of the installed app.
* Custom dashboards (no default Django admin) and drag-and-drop upload UX.
* TailwindCSS UI, token-secure settings via `.env`.

---

## ✨ Features

| Module            | Highlights                                             |
|-------------------|--------------------------------------------------------|
| Authentication    | Django auth with custom `CustomUser` (+ `is_admin`)    |
| Admin Dashboard   | Add apps, review screenshots, approve/credit points    |
| User Dashboard    | List apps, total points, tasks completed               |
| Drag & Drop       | Vanilla-JS drag-and-drop screenshot upload             |
| Media Handling    | Local `media/`; easy to switch to S3                   |
| Decorators        | `@admin_required` utility keeps views clean            |

---

## 🛠️ Developer Quick-Start

> **Prereqs**: Python 3.11+, Git, (optional) `virtualenv`

1. **Clone & enter the repo**

   ```bash
   git clone https://github.com/<you>/nextlabs.git
   cd nextlabs
