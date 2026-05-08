# I18nForge

🎉 **README 다국어 지능형 생성기** | Markdown-aware README translation tool with format preservation

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Stars](https://img.shields.io/github/stars/gitstq/I18nForge)](https://github.com/gitstq/I18nForge/stargazers)

[🇨🇳 简体中文](README_zh-CN.md) | [🇹🇼 繁體中文](README_zh-TW.md) | [🇺🇸 English](README.md) | [🇯🇵 日本語](README_ja.md) | **🇰🇷 한국어** | [🇪🇸 Español](README_es.md)

---

## 🎉 프로젝트 소개

**I18nForge**는 GitHub README를 위해 설계된**다국어 지능형 생성기**입니다. Markdown 형식을 지능적으로 인식하고, 이모지, 코드 블록, 링크 등의 특수 요소를 유지하면서 여러 언어로 콘텐츠를 번역합니다.

### ✨ 해결하는 문제

- 📝 수동 README 번역은 시간이 많이 소요됩니다
- 🎨 번역 후 형식이 깨지고 이모지가 사라집니다
- 🔗 링크와 코드 블록이 잘못 번역됩니다
- 🌐 다국어 버전이 필요하지만 적절한 도구가 없습니다

### 🚀 자사 차별화 포인트

1. **Markdown 인식 파싱** - 제목, 목록, 코드 블록, 테이블을 지능적으로 식별
2. **형식 100% 유지** - 이모지, Markdown 구문, 코드 블록 완전 보존
3. **제로 의존성 설계** - 순수 Python 표준 라이브러리, 외부 의존성 없음
4. **다중 번역 엔진** - Mock, Google, DeepL, OpenAI 등 다양한 번역 서비스 지원
5. **언어 자동 전환** - 언어 전환 버튼 생성, 쉬운 전환实现

## ✨ 핵심 기능

| 기능 | 설명 |
|------|------|
| 🎨 **Markdown 인식** | Markdown 구조를 지능적으로 파싱하고 번역 가능 콘텐츠와 서식 요소 구분 |
| 😊 **이모지 보존** | 100% 이모지 보존, 시각적 요소 손실 없음 |
| 💻 **코드 블록 보호** | 코드 블록 콘텐츠는 번역되지 않으며 원본 코드 유지 |
| 🔗 **링크 지능형 처리** | 링크와 이미지는 잘못 번역되지 않음 |
| 📊 **테이블 지원** | 완전한 Markdown 테이블 번역 지원 |
| 🌐 **다국어 전환** | 언어 전환 버튼 자동 생성, 원클릭 전환 |
| ⚡ **제로 의존성** | 순수 Python 표준 라이브러리 구현, 추가 패키지 불필요 |
| 🔧 **다중 엔진** | Mock, Google, DeepL, OpenAI 등 다양한 번역 엔진 지원 |
| 💾 **지능형 캐싱** | 번역 결과를 로컬 캐싱, 중복 번역 회피 |
| 🎯 **증분 번역** | 새로 추가되거나 수정된 콘텐츠만 번역, 시간과 비용 절약 |

## 🚀 빠른 시작

### 📋 동작 환경

- Python 3.8+
- 추가 의존성 없음 (제로 의존성 설계)

### 💾 설치

**방법 1: pip 설치**

```bash
pip install i18nforge
```

**방법 2: 소스에서 설치**

```bash
git clone https://github.com/gitstq/I18nForge.git
cd I18nForge
pip install -e .
```

### 📖 기본 사용법

**CLI 사용**

```bash
# 영어로 번역
i18nforge translate README.md -t en

# 여러 언어로 번역
i18nforge translate README.md -t en,ja,ko

# 지정 번역 엔진 사용
i18nforge translate README.md -t en --engine google
```

**README 템플릿 생성**

```bash
i18nforge generate -n MyProject -d "이것은素晴らしい 프로젝트입니다" -f "경량" -f "사용하기 쉬움"
```

### ⚙️ CLI 옵션

```
사용법: i18nforge [명령] [옵션]

명령:
  translate     README 파일 번역
  generate     README 템플릿 생성
  languages    지원되는 언어 목록 표시

옵션:
  -t, --target        대상 언어 (쉼표로 구분)
  -s, --source        소스 언어 (기본값: zh-CN)
  -o, --output        출력 디렉토리 (기본값: 현재 디렉토리)
  -e, --engine        번역 엔진 (mock/google/deepl/openai)
  -k, --api-key       API 키
  --no-switcher       언어 전환 버튼 생성 안 함
```

## 💡 설계 철학 및 로드맵

### 설계 원칙

1. **제로 의존성 우선** - Python 표준 라이브러리 우선, 사용 장벽 감소
2. **형식 지상** - 번역 중에 원본 Markdown 형식을 손상시키지 않음
3. **점진적 향상** - 기본 기능은 제로 의존성, 고급 기능은 선택적
4. **사용자 친화적** - 깔끔한 CLI 인터페이스, 사용하기 쉬움

### 아키텍처

```
┌─────────────────────────────────────────┐
│           I18nForge                      │
├─────────────────────────────────────────┤
│  ┌─────────┐  ┌──────────┐  ┌────────┐ │
│  │  CLI    │  │ Generator │  │ Config │ │
│  └────┬────┘  └────┬─────┘  └────────┘ │
│       │            │                    │
│  ┌────┴────┐  ┌────┴─────┐             │
│  │ Parser  │  │Translator│             │
│  └─────────┘  └──────────┘             │
└─────────────────────────────────────────┘
```

### 향후 로드맵

- [ ] v1.1 - 다른 Markdown 구문 지원 (각주, 작업 목록)
- [ ] v1.2 - 웹 인터페이스 추가
- [ ] v1.3 - 이미지 내 텍스트 OCR 번역 지원
- [ ] v2.0 - AI 기반 컨텍스트 인식 번역
- [ ] v2.1 - GitHub Actions 자동 번역 통합
- [ ] v2.2 - 커뮤니티 번역 템플릿 마켓플레이스

## 🤝 기여 가이드

코드 기여를 환영합니다! 다음 단계를 따르세요:

1. 이 저장소를 Fork
2. 기능 브랜치 생성 (`git checkout -b feature/amazing-feature`)
3. 변경 사항 커밋 (`git commit -m 'Add amazing feature'`)
4. 브랜치에 푸시 (`git push origin feature/amazing-feature`)
5. Pull Request 생성

### 개발 환경 설정

```bash
# 저장소 복제
git clone https://github.com/gitstq/I18nForge.git
cd I18nForge

# 개발 의존성 설치
pip install -e ".[dev]"

# 테스트 실행
pytest tests/

# 코드 포맷팅
black i18nforge/
flake8 i18nforge/
```

## 📄 라이선스

이 프로젝트는 **MIT 라이선스**로 라이선스되어 있습니다:

✅ 이 소프트웨어의 자유로운 사용, 수정, 배포
✅ 상업적 사용
✅ 개인 프로젝트에서 사용

详细内容은 [LICENSE](LICENSE)를 참조하세요.

---

<p align="center">
  <strong>Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a></strong>
  <br>
  <sub>이 프로젝트가 도움이 되셨다면 ⭐을 눌러주세요</sub>
</p>
