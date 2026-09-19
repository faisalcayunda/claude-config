---
title: "Data Science Model — <Nama Model>"
sidebar_label: "Data Science Model"
sidebar_position: 8
description: "Model card dan dokumentasi deployment model machine learning: algoritma, training data, performa, monitoring drift, dan panduan penggunaan."
tags: [development, machine-learning, model-card, mlops, data-science]
doc_id: "V-08"
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: development
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Data Science Model

> **Tujuan dokumen ini:** Model card yang mendokumentasikan model ML yang dibangun di atas data product ini — mencakup tujuan, metodologi, performa aktual, batasan, dan panduan deployment serta monitoring.

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Model card awal post-deployment | `<Nama, Role>` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | `V-08` |
| **Domain** | `<Nama Domain>` |
| **Data Product** | `<Nama Data Product>` |
| **Nama Model** | `<Nama deskriptif model>` |
| **Model ID** | `<urn:dp:<domain>:<product>:model:<nama>:v<N>>` |
| **Tipe Model** | `<Klasifikasi / Regresi / Clustering / Ranking / Anomaly Detection>` |
| **Framework** | `<scikit-learn / XGBoost / LightGBM / PyTorch / TensorFlow>` |
| **Versi Model** | `v<N>` |
| **Status** | `<Production / Staging / Deprecated>` |
| **Model Registry** | `<MLflow / SageMaker / Vertex AI: link ke experiment>` |
| **Data Scientist** | `<Nama, Email>` |
| **Dokumen terkait** | [D-04 Data Catalog](../design/data-catalog.md) · [D-05 Quality Design](../design/quality-design.md) · [V-05 Data Pipeline](./data-pipeline.md) |

---

## 1. Model Overview

### 1.1 Tujuan dan Use Case

`[Mandatory]`

> `[Deskripsikan: apa yang diprediksi/diklasifikasikan, mengapa model ini dibutuhkan, dan bagaimana outputnya digunakan dalam proses bisnis.]`

**Input:** `<Deskripsi data input — tabel/fitur apa yang dikonsumsi>`
**Output:** `<Deskripsi prediksi/skor/label yang dihasilkan>`
**Consumer output model:** `<Sistem / tim yang menggunakan hasil model>`

### 1.2 Batasan dan Situasi Tidak Sesuai

:::warning Batasan Model
Model ini **tidak sesuai** untuk:
- `<Use case yang out-of-scope — contoh: data dari wilayah yang tidak ada di training set>`
- `<Populasi yang under-represented di training data>`
- `<Penggunaan di luar konteks bisnis yang sudah divalidasi>`
:::

---

## 2. Data Training

### 2.1 Dataset yang Digunakan

| Dataset | Sumber | Periode | Jumlah Record | Keterangan |
|---|---|---|---|---|
| Training set | `<schema>.v_<product>_daily` | `<YYYY-MM s.d. YYYY-MM>` | `<N>` | 80% split |
| Validation set | `<schema>.v_<product>_daily` | `<YYYY-MM s.d. YYYY-MM>` | `<N>` | 10% split |
| Test set (holdout) | `<schema>.v_<product>_daily` | `<YYYY-MM s.d. YYYY-MM>` | `<N>` | 10% split, tidak disentuh sampai evaluasi final |

### 2.2 Feature Engineering

| Fitur | Tipe | Sumber | Transformasi | Importance Rank |
|---|---|---|---|---|
| `<fitur_1>` | `Numerik` | `<kolom>` | `StandardScaler` | `1` |
| `<fitur_2>` | `Kategorikal` | `<kolom>` | `OrdinalEncoder` | `3` |
| `<fitur_3>` | `Derived` | `<formula>` | `Log transform` | `2` |
| `<fitur_N>` | `<tipe>` | `<sumber>` | `<transform>` | `<rank>` |

### 2.3 Label / Target Variable

| Atribut | Nilai |
|---|---|
| Nama kolom target | `<nama_kolom>` |
| Tipe | `<Binary / Multiclass / Continuous>` |
| Distribusi (training) | `<Positif: X%, Negatif: Y%>` (untuk klasifikasi) |
| Catatan imbalance | `<Apakah ada class imbalance? Bagaimana ditangani?>` |

---

## 3. Algoritma dan Hyperparameter

### 3.1 Algoritma yang Dipilih

**Algoritma final:** `<Nama algoritma>`

**Justifikasi pemilihan:**
> `[Jelaskan mengapa algoritma ini dipilih vs alternatif yang dicoba. Sertakan trade-off interpretability vs performance.]`

**Alternatif yang dievaluasi:**

| Algoritma | Metric Utama | Alasan Tidak Dipilih |
|---|---|---|
| `<Logistic Regression>` | `<AUC: 0.78>` | `<Performa lebih rendah, tapi dipertahankan sebagai baseline>` |
| `<XGBoost>` | `<AUC: 0.89>` | `<Model akhir yang dipilih>` |
| `<Neural Network>` | `<AUC: 0.87>` | `<Lebih sulit diinterpretasikan, performa tidak signifikan lebih baik>` |

### 3.2 Hyperparameter Final (Production)

```python
params = {
    "<param_1>": <nilai>,
    "<param_2>": <nilai>,
    "<param_3>": <nilai>,
    # Ditemukan via Optuna / GridSearch
    # Experiment: <link ke MLflow experiment>
}
```

---

## 4. Evaluasi Performa

### 4.1 Metric Utama

| Metric | Test Set | Validation Set | Target Minimum | Status |
|---|---|---|---|---|
| `<AUC-ROC>` | `<0.891>` | `<0.887>` | `<0.85>` | ✅ |
| `<Precision>` | `<0.82>` | `<0.81>` | `<0.75>` | ✅ |
| `<Recall>` | `<0.76>` | `<0.74>` | `<0.70>` | ✅ |
| `<F1-Score>` | `<0.79>` | `<0.77>` | `<0.72>` | ✅ |

### 4.2 Analisis Bias dan Fairness

`[Mandatory untuk model yang mempengaruhi keputusan tentang individu]`

| Subgroup | Metric | Nilai | Vs Keseluruhan | Status |
|---|---|---|---|---|
| `<Wilayah A>` | AUC | `<0.88>` | `-0.01` | ✅ Acceptable |
| `<Wilayah B>` | AUC | `<0.79>` | `-0.10` | ⚠️ Perlu perhatian |

---

## 5. Deployment

### 5.1 Arsitektur Deployment

| Komponen | Detail |
|---|---|
| Serving mode | `<Batch scoring harian / Real-time API / Embedded dalam pipeline>` |
| Endpoint | `<https://ml-api.<domain>.org/v1/models/<model-name>/predict>` (jika real-time) |
| Batch schedule | `<Setiap hari jam 03:00 WIB>` (jika batch) |
| Output disimpan di | `<schema>.model_scores_<product>` |
| Model artifact | `<s3://<bucket>/models/<nama>/<version>/model.pkl>` |
| MLflow tracking | `<https://mlflow.<domain>.org/experiments/<id>>` |

### 5.2 Schema Output Scoring

| Kolom | Tipe | Keterangan |
|---|---|---|
| `entity_id` | `UUID` | ID entitas yang di-score |
| `score` | `FLOAT` | Skor probabilitas 0–1 |
| `label` | `VARCHAR` | Label prediksi (`positif` / `negatif`) |
| `score_threshold` | `FLOAT` | Threshold yang digunakan saat scoring |
| `model_version` | `VARCHAR` | Versi model yang menghasilkan skor ini |
| `scored_at` | `TIMESTAMPTZ` | Waktu scoring |

---

## 6. Monitoring Model

### 6.1 Metrik yang Dipantau

| Metrik | Tool | Threshold Alert | Frekuensi |
|---|---|---|---|
| Data drift (input features) | `<Evidently / Whylogs>` | PSI > 0.2 | Harian |
| Prediction drift (output distribution) | `<Evidently>` | KL divergence > 0.1 | Harian |
| Model performance (jika ada ground truth) | `<Custom SQL>` | AUC drop > 5% dari baseline | Mingguan |
| Latency scoring | Grafana | P95 > 200ms | Real-time |

### 6.2 Jadwal Retraining

| Trigger | Kondisi | Tindakan |
|---|---|---|
| Scheduled | Setiap `<3 bulan>` | Full retrain dengan data terbaru |
| Drift alert | PSI > 0.2 atau AUC drop > 5% | Evaluasi → retrain jika diperlukan |
| Data schema change | Kolom fitur berubah di source | Wajib retrain sebelum deploy |

---

## Annex A — Reproducibility

```bash
# Clone repo
git clone https://github.com/org/<repo>.git
cd <repo>/models/<model-name>

# Checkout versi spesifik
git checkout <git-tag-versi-model>

# Install dependencies
pip install -r requirements.txt

# Reproduce training
python train.py --config configs/production.yaml

# Evaluate
python evaluate.py --model-path outputs/model.pkl --test-data data/test.parquet
```

Seed untuk reproducibility: `random_state = <42>` di semua komponen.
