# I18nForge

🎉 **Generador Inteligente Multilingüe de README** | Herramienta de traducción de Markdownaware con preservación de formato

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Stars](https://img.shields.io/github/stars/gitstq/I18nForge)](https://github.com/gitstq/I18nForge/stargazers)

[🇨🇳 简体中文](README_zh-CN.md) | [🇹🇼 繁體中文](README_zh-TW.md) | [🇺🇸 English](README.md) | [🇯🇵 日本語](README_ja.md) | [🇰🇷 한국어](README_ko.md) | **🇪🇸 Español**

---

## 🎉 Introducción del Proyecto

**I18nForge** es un **generador inteligente multilingüe** diseñado específicamente para archivos README de GitHub. Reconoce inteligentemente el formato Markdown, preserva elementos especiales como emojis, bloques de código y enlaces, mientras traduce el contenido a múltiples idiomas.

### ✨ Problemas que Resolvemos

- 📝 La traducción manual de README consume mucho tiempo
- 🎨 El formato se rompe después de la traducción, los emojis se pierden
- 🔗 Los enlaces y bloques de código se traducen incorrectamente
- 🌐 Necesitas versiones multilingües pero no hay buenas herramientas

### 🚀 Diferenciadores Clave

1. **Análisis Consciente de Markdown** - Identifica inteligentemente títulos, listas, bloques de código, tablas
2. **Preservación del Formato 100%** - Emojis, sintaxis Markdown, bloques de código completamente preservados
3. **Diseño Sin Dependencias** - Librería estándar pura de Python, sin dependencias externas
4. **Múltiples Motores de Traducción** - Soporta Mock, Google, DeepL, OpenAI y más
5. **Conmutador de Idioma Automático** - Genera selector de idioma para cambiar fácilmente

## ✨ Características Principales

| Característica | Descripción |
|----------------|-------------|
| 🎨 **Consciente de Markdown** | Análisis inteligente de estructura Markdown, distingue contenido traducible |
| 😊 **Preservación de Emojis** | 100% preservación de emojis, sin pérdida de elementos visuales |
| 💻 **Protección de Bloques de Código** | Los bloques de código no se traducen, código original preservado |
| 🔗 **Manejo Inteligente de Enlaces** | Enlaces e imágenes no se traducen incorrectamente |
| 📊 **Soporte de Tablas** | Soporte completo de traducción de tablas Markdown |
| 🌐 **Conmutador Multilingüe** | Genera selector de idioma automáticamente, cambio con un clic |
| ⚡ **Sin Dependencias** | Implementación con librería estándar pura de Python, sin paquetes extra |
| 🔧 **Múltiples Motores** | Soporta Mock, Google, DeepL, OpenAI y más |
| 💾 **Caché Inteligente** | Caché local de resultados de traducción, evita repeticiones |
| 🎯 **Traducción Incremental** | Solo traduce contenido nuevo o modificado, ahorra tiempo |

## 🚀 Inicio Rápido

### 📋 Requisitos del Entorno

- Python 3.8+
- Sin dependencias adicionales (diseño sin dependencias)

### 💾 Instalación

**Método 1: Instalación con pip**

```bash
pip install i18nforge
```

**Método 2: Desde código fuente**

```bash
git clone https://github.com/gitstq/I18nForge.git
cd I18nForge
pip install -e .
```

### 📖 Uso Básico

**Uso de CLI**

```bash
# Traducir a inglés
i18nforge translate README.md -t en

# Traducir a múltiples idiomas
i18nforge translate README.md -t en,ja,ko

# Usar motor de traducción específico
i18nforge translate README.md -t en --engine google
```

**Generar Plantilla README**

```bash
i18nforge generate -n MyProject -d "Este es un proyecto increíble" -f "Ligero" -f "Fácil de usar"
```

### ⚙️ Opciones de CLI

```
Uso: i18nforge [comando] [opciones]

Comandos:
  translate     Traducir archivo README
  generate      Generar plantilla README
  languages     Mostrar lista de idiomas soportados

Opciones:
  -t, --target        Idiomas destino (separados por comas)
  -s, --source        Idioma origen (predeterminado: zh-CN)
  -o, --output        Directorio de salida (predeterminado: actual)
  -e, --engine        Motor de traducción (mock/google/deepl/openai)
  -k, --api-key       Clave API
  --no-switcher       No generar selector de idioma
```

## 💡 Filosofía de Diseño y Hoja de Ruta

### Principios de Diseño

1. **Primero Sin Dependencias** - Priorizar librería estándar de Python, reducir barrera de uso
2. **Formato es Rey** - No romper formato Markdown original durante traducción
3. **Mejora Progresiva** - Funciones básicas sin dependencias, funciones avanzadas opcionales
4. **Amigable al Usuario** - Interfaz CLI limpia, fácil de usar

### Arquitectura

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

### Hoja de Ruta Futura

- [ ] v1.1 - Soporte para más sintaxis Markdown (notas al pie, listas de tareas)
- [ ] v1.2 - Agregar interfaz web
- [ ] v1.3 - Soporte de traducción OCR para texto en imágenes
- [ ] v2.0 - Traducción consciente del contexto impulsada por IA
- [ ] v2.1 - Integración de traducción automática con GitHub Actions
- [ ] v2.2 - Mercado de plantillas de traducción de la comunidad

## 🤝 Guía de Contribución

¡Damos la bienvenida a las contribuciones! Por favor sigue estos pasos:

1. Haz fork de este repositorio
2. Crea una rama de característica (`git checkout -b feature/amazing-feature`)
3. Confirma tus cambios (`git commit -m 'Add amazing feature'`)
4. Haz push a la rama (`git push origin feature/amazing-feature`)
5. Crea un Pull Request

### Configuración del Entorno de Desarrollo

```bash
# Clonar el repositorio
git clone https://github.com/gitstq/I18nForge.git
cd I18nForge

# Instalar dependencias de desarrollo
pip install -e ".[dev]"

# Ejecutar pruebas
pytest tests/

# Formatear código
black i18nforge/
flake8 i18nforge/
```

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Eres libre de:

✅ Usar, modificar y distribuir este software
✅ Uso comercial
✅ Proyectos privados

Ver [LICENSE](LICENSE) para más detalles.

---

<p align="center">
  <strong>Hecho con ❤️ por <a href="https://github.com/gitstq">gitstq</a></strong>
  <br>
  <sub>Si este proyecto te resulta útil, por favor dale una ⭐</sub>
</p>
