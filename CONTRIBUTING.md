# Contributing to Loxs

Thank you for your interest in contributing to Loxs! This document provides guidelines for contributing to the project.

## Getting Started

1. **Fork the repository** to your GitHub account
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/loxs.git
   cd loxs
   ```
3. **Add the upstream remote**:
   ```bash
   git remote add upstream https://github.com/coffinxp/loxs.git
   ```

## Development Setup

1. **Install Python dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Install Chrome/Chromium** (required for XSS scanning):
   - On Ubuntu/Debian: `sudo apt install google-chrome-stable`
   - On other systems, download from the official website

3. **Test the installation**:
   ```bash
   python3 loxs.py
   ```

## Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following these guidelines:
   - Write clear, readable code
   - Add docstrings to functions and classes
   - Follow PEP 8 style guidelines
   - Test your changes thoroughly

3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

## Contribution Guidelines

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and reasonably sized

### Commit Messages
Use conventional commit format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for adding tests

### Areas for Contribution

1. **Code Quality Improvements**:
   - Refactoring large functions
   - Improving error handling
   - Adding type hints
   - Code documentation

2. **New Features**:
   - Additional vulnerability scanners
   - Better reporting formats
   - Configuration improvements
   - Performance optimizations

3. **Bug Fixes**:
   - Check the Issues tab for reported bugs
   - Test edge cases and fix crashes

4. **Documentation**:
   - Improve existing documentation
   - Add usage examples
   - Create tutorials

### Testing

Before submitting your contribution:

1. **Test basic functionality**:
   ```bash
   python3 loxs.py
   ```

2. **Test your specific changes** with various inputs

3. **Check for any new errors or warnings**

## Submitting Changes

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** from your fork to the main repository

3. **Provide a clear description** of your changes:
   - What problem does it solve?
   - How did you test it?
   - Any breaking changes?

## Code of Conduct

- Be respectful and constructive in discussions
- Help others learn and grow
- Focus on what's best for the community
- Show empathy towards other contributors

## Questions?

If you have questions about contributing:
- Open an issue with the "question" label
- Reach out to the maintainers
- Check existing issues and discussions

Thank you for contributing to Loxs! 🔍🔒
