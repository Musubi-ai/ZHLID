# ZHLID: Fine-grained Chinese Language Identification Package
ZHLID is an open-source, model-based language identification tool specialized in fine-grained Chinese varieties.

## Features
Unlike general-purpose LID tools, ZHLID focuses on distinguishing between closely related Chinese varieties, including:

**Traditional Chinese (繁體中文)** – written in the traditional character set, used in formal and classical texts.  
**Simplified Chinese (簡體中文)** – written in the simplified character set, designed for easier reading and writing.  
**Cantonese (粵語)** – written form reflecting spoken Cantonese with unique vocabulary and grammar.  
**Classical Chinese (Traditional) (繁體文言文)** – literary Chinese in traditional characters with concise, classical syntax.  
**Classical Chinese (Simplified) (簡體文言文)** – literary Chinese in simplified characters, used in modern reprints and education.

This makes ZHLID useful for linguistic research, corpus analysis, preprocessing for NLP tasks, or any application requiring accurate recognition of Chinese textual forms.

The following table compares ZHLID with other popular LID tools supporting Chinese detection:

| Identification | General Chinese | Traditional Chinese | Simplified Chinese | Classical Chinese | Cantonese |
|------|:----:|:----:|:----:|:----:|:----:|
| ZHLID (ours) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [langdetect](https://github.com/Mimino666/langdetect) | ✅ | ✅ | ✅ | ❌ | ❌ |
| [GlotLID](https://github.com/cisnlp/GlotLID/tree/main) | ✅ | ❌ |❌ |❌ | ✅ |
| [langid.py](https://github.com/saffsd/langid.py) | ✅ | ❌ | ❌ | ❌ | ❌ |
| [CLD3](https://github.com/google/cld3?tab=readme-ov-file#supported-languages) | ✅ | ❌ | ❌ | ❌ | ❌ |
| [Lingua](https://github.com/pemistahl/lingua-py) | ✅ | ❌ | ❌ | ❌ | ❌ |

## Installation
### Install via pip
```bash
pip install zhlid
```

### Install from source
```bash
pip install git+https://github.com/Musubi-ai/ZHLID
```

## Usage
```python
from zhlid import load_model


model = load_model("MusubiAI/ZHLID", device_map="auto")

text = [
    "王夫之者，字而農，衡陽人，明末清初哲學家。張獻忠陷衡州，夫之匿南嶽，賊執其父以為質。夫之自引刀遍刺肢體，舁往易父。",
    "金山阿伯係清末民初時嘅一種現象。金山阿伯係指嗰啲生活喺廣東地方，因為搵唔夠錢畀家人生活，要出洋到舊金山或新金山做苦工，掘金礦。",
    "燧人氏，古之三皇，有巢氏之子。 风姓，讳允婼，华夏族。燧人钻火，教人熟食，立国曰燧明，为后世奉为「火祖」，号燧皇。立一百一十年，崩，子伏羲嗣。\n\n**引据**\n《风俗通义·皇霸篇》\n*",
    "在量子力学中，量子涨落（quantum fluctuation。或量子真空涨落，真空涨落）是在空间任意位置对于能量的暂时变化。 \n从维尔纳·海森堡的不确定性原理可以推导出这结论。",
    "在政治中，政治議程是政府官員以及政府以外的個人在任何給定時間都認真關注的主題或問題/議題的列表。"
]

res = model.predict(text, batch_size=5)
print(res)
# [
#     {'label': 'zhtw_classical', 'confidence_score': 0.9999634027}, 
#     {'label': 'yue', 'confidence_score': 0.9376096725}, 
#     {'label': 'zhcn_classical', 'confidence_score': 0.9999793768}, 
#     {'label': 'zhcn', 'confidence_score': 0.9944804907}, 
#     {'label': 'zhtw', 'confidence_score': 0.9998573065}
# ]
```
## Evaluation
To evaluate ZHLID with our benchmark dataset, simply run:
```bash
python evaluate.py
```

We compare our top-1 accuracy result with [GlotLID](https://github.com/cisnlp/GlotLID/tree/main) and [langdetect](https://github.com/Mimino666/langdetect). Note that since GlotLID only provides a general "cmn_Hani" label for Chinese, its performance on Traditional and Simplified Chinese is measured by whether it outputs this label for both categories.

| Top-1 acc | Traditional Chinese | Simplified Chinese | Classical Chinese (Traditional) | Classical Chinese (Simplified) | Cantonese |
|------|:----:|:----:|:----:|:----:|:----:|
| ZHLID (ours) | 1.0 | 1.0 | 0.9 | 1.0 | 0.96 |
| [GlotLID](https://github.com/cisnlp/GlotLID/tree/main) | 0.98 | 0.98 | - | - | 0.9 |
| [langdetect](https://github.com/Mimino666/langdetect) | 0.3 | 0.9 | - | - | - |

## Citation
If you use ZHLID in your research, please cite this repository:
```bibtex
@misc{zhlid2025 ,
  title  = {ZHLID: Fine-grained Chinese Language Identification Package},
  author = {Lung-Chuan Chen},
  year   = {2025},
  howpublished = {\url{https://github.com/Musubi-ai/ZHLID}}
}
```