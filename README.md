# 🐱🌪️ CatHurricane (고양이 태풍)

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=250&section=header&text=Cat%20Hurricane&fontSize=70&animation=fadeIn&fontAlignY=38" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Pillow-Image-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
</p>

<p align="center">
  <b>모니터 테두리를 무한 질주하는 귀여운 고양이 밈(Meme) 대축제!</b><br>
  바쁜 작업 공간 속에 소소한 힐링을 선사하는 투명 오버레이 데스크톱 펫 애플리케이션입니다.
</p>

---

## ⚡ 주요 특징 (Key Features)

* **✨ 완벽한 배경 투명화**: 바탕화면 위에서 작업창을 가리지 않고 자연스럽게 고양이들이 달립니다.
* **🏃 개성 넘치는 속도와 크기**: 고양이마다 크기와 달리는 속도가 랜덤하게 부여되어 짜릿한 추격전(?)이 연출됩니다.
* **🚂 기차놀이 스타트 딜레이**: 소환 시간에 시차를 두어 고양이들이 겹치지 않고 꼬리를 물며 달리는 장관을 이룹니다.
* **❌ 안전 장치 탑재**: 너무 정신없거나 부장님이 뒤에 오시면 언제든 `ESC` 키를 눌러 순식간에 종료할 수 있습니다.

---

## 🎮 포함된 고양이 라인업 (Cat Lineup)

현재 태풍을 구성하고 있는 정예 멤버들입니다.

* `spinning-maxwell.gif` (빙글빙글 도는 맥스웰)
* `banana-cat-cat-banana.gif` (우는 바나나 고양이)
* `popcat.gif` (입을 뻐끔거리는 팝캣)
* `stresscat.gif` / `nyangcat.gif` / `huh.gif` / `giphy.gif` / `cool-fun.gif`

---

## 🚀 시작하기 (Quick Start)

### 1. 필수 라이브러리 설치
이 프로젝트는 이미지 처리를 위해 `Pillow` 라이브러리가 필요합니다.

```bash
pip install Pillow

## 2. 실행하기

GIF 파일들이 있는 폴더에서 아래 명령어를 실행하면 고양이 태풍이 시작됩니다.

```bash
python cat_runner.py
```

### 종료 방법

고양이가 달리는 화면을 한 번 클릭한 상태로 `ESC` 키를 누르면 종료됩니다.

---

## 기술 스택

| 구분 | 기술 / 라이브러리 | 용도 |
|---|---|---|
| Language | Python 3.10+ | 메인 로직 개발 |
| GUI Framework | Tkinter | 화면 렌더링, 투명 윈도우 및 최상단 오버레이 구현 |
| Image Process | Pillow, PIL | GIF 파일 분석, 개별 프레임 분리 및 리사이징 순회 |

---

## 커스텀 방법

원하는 GIF 파일을 추가해서 나만의 고양이 군단을 만들 수 있습니다.

### 1. GIF 파일 추가

원하는 고양이 GIF 파일을 프로젝트 루트 폴더에 넣습니다.

```text
project-root/
├── cat_runner.py
├── spinning-maxwell.gif
├── banana-cat-cat-banana.gif
├── my-lovely-cat.gif
└── another-cat.gif
```

### 2. 코드에 파일명 추가

`cat_runner.py` 파일을 열고, 코드 내부의 `self.meme_files` 리스트에 새 GIF 파일명을 추가합니다.

```python
# cat_runner.py 파일 내부 예시

self.meme_files = [
    "spinning-maxwell.gif",
    "banana-cat-cat-banana.gif",
    "my-lovely-cat.gif",   # 직접 추가한 파일명
    "another-cat.gif"      # 직접 추가한 파일명
]
```

### 3. 다시 실행

파일을 추가한 뒤 아래 명령어로 다시 실행합니다.

```bash
python cat_runner.py
```
