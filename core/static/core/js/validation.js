// core/static/core/js/validation.js

// Функция для показа ошибки поля
function showFieldError(field, message) {
    field.style.borderColor = '#ff0000';
    field.style.boxShadow = '0 0 5px rgba(255, 0, 0, 0.5)';

    // Удаляем старое сообщение об ошибке
    const oldError = field.parentElement.querySelector('.field-error');
    if (oldError) {
        oldError.remove();
    }

    // Добавляем новое сообщение
    if (message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'field-error';
        errorDiv.style.color = '#ff0000';
        errorDiv.style.fontSize = '12px';
        errorDiv.style.marginTop = '5px';
        errorDiv.textContent = message;
        field.parentElement.appendChild(errorDiv);
    }
}

// Функция для очистки ошибки
function clearFieldError(field) {
    field.style.borderColor = '#00ff00';
    field.style.boxShadow = '0 0 5px rgba(0, 255, 0, 0.5)';

    const error = field.parentElement.querySelector('.field-error');
    if (error) {
        error.remove();
    }
}

// Форматирование даты
function formatDateInput(field) {
    let value = field.value.replace(/\D/g, ''); // Удаляем все нецифровые символы
    let formatted = '';

    // Ограничиваем длину до 8 цифр (ДДММГГГГ)
    value = value.substring(0, 8);

    if (value.length >= 2) {
        formatted = value.substring(0, 2);
        if (value.length > 2) {
            formatted += '.';
            formatted += value.substring(2, 4);
        }
        if (value.length > 4) {
            formatted += '.';
            formatted += value.substring(4, 8);
        }
    } else {
        formatted = value;
    }

    field.value = formatted;

    // Валидация после форматирования
    if (formatted.length === 10) {
        validateDate(field);
    }
}

function validateDate(field) {
    const value = field.value;
    const pattern = /^(\d{2})\.(\d{2})\.(\d{4})$/;

    if (!pattern.test(value)) {
        showFieldError(field, 'Формат: ДД.ММ.ГГГГ');
        return false;
    }

    const [_, day, month, year] = value.match(pattern);
    const date = new Date(year, month - 1, day);

    if (date.getDate() != day || date.getMonth() + 1 != month || date.getFullYear() != year) {
        showFieldError(field, 'Некорректная дата');
        return false;
    }

    clearFieldError(field);
    return true;
}

function validateFIO(input) {
    const value = input.value.trim();

    // Разрешаем только буквы (русские и английские), пробелы и дефис
    const validCharsPattern = /^[а-яА-ЯёЁa-zA-Z\-\s]*$/;

    // Проверяем каждый введенный символ
    if (!validCharsPattern.test(value)) {
        // Удаляем недопустимые символы
        input.value = value.replace(/[^а-яА-ЯёЁa-zA-Z\-\s]/g, '');
        showFieldError(input, 'Только буквы и дефис');
        return;
    }

    // Проверка на двойные дефисы
    if (value.includes('--')) {
        input.value = value.replace(/--+/g, '-');
        showFieldError(input, 'Недопустимы двойные дефисы');
        return;
    }

    // Проверка на дефис в начале или конце слова
    const words = value.split(/\s+/);
    for (let word of words) {
        if (word.startsWith('-') || word.endsWith('-')) {
            showFieldError(input, 'Слова не могут начинаться или заканчиваться дефисом');
            return;
        }
    }

    // Базовые проверки
    if (value.length < 5) {
        showFieldError(input, 'ФИО слишком короткое');
        return;
    }

    if (value.length > 50) {
        showFieldError(input, 'ФИО слишком длинное');
        return;
    }

    const parts = value.split(/\s+/).filter(p => p.length > 0);
    if (parts.length < 2) {
        showFieldError(input, 'Введите минимум фамилию и имя');
        return;
    }

    // Проверка на максимум 3 части (Фамилия Имя Отчество)
    if (parts.length > 3) {
        showFieldError(input, 'ФИО должно содержать максимум 3 части (Фамилия Имя Отчество)');
        return;
    }

    // Проверяем, что каждая часть начинается с заглавной буквы
    for (let part of parts) {
        if (part.length > 0 && part[0] !== part[0].toUpperCase()) {
            showFieldError(input, 'Каждая часть ФИО должна начинаться с заглавной буквы');
            return;
        }
    }

    clearFieldError(input);
}

function restrictFIOInput(input) {
    // Устанавливаем максимальную длину
    input.maxLength = 50;

    // Блокируем недопустимые символы при вводе
    input.addEventListener('keypress', function(e) {
        const char = String.fromCharCode(e.which || e.keyCode);

        // Если это пробел
        if (char === ' ') {
            // Подсчитываем количество пробелов в текущем значении
            const currentSpaces = (this.value.match(/ /g) || []).length;

            // Если уже есть 2 пробела, блокируем ввод
            if (currentSpaces >= 2) {
                e.preventDefault();
                showFieldError(this, 'Максимум 3 части ФИО');
                return false;
            }

            // Не даем вводить пробел в начале
            if (this.value.length === 0) {
                e.preventDefault();
                return false;
            }

            // Не даем вводить два пробела подряд
            if (this.value[this.value.length - 1] === ' ') {
                e.preventDefault();
                return false;
            }
        }

        // Блокируем все символы кроме букв, дефиса и пробела
        const pattern = /^[а-яА-ЯёЁa-zA-Z\-]$/;
        if (!pattern.test(char) && char !== ' ') {
            e.preventDefault();
            return false;
        }
    });

    input.addEventListener('input', function(e) {
        // Удаляем недопустимые символы
        let value = this.value.replace(/[^а-яА-ЯёЁa-zA-Z\-\s]/g, '');

        // Заменяем множественные пробелы на одинарные
        value = value.replace(/\s+/g, ' ');

        // Проверяем количество пробелов после очистки
        const spaces = (value.match(/ /g) || []).length;

        // Если больше 2 пробелов, обрезаем
        if (spaces > 2) {
            const parts = value.split(' ');
            value = parts.slice(0, 3).join(' ');
        }

        this.value = value;
        validateFIO(this);
    });

    // Блокируем вставку с проверкой
    input.addEventListener('paste', function(e) {
        e.preventDefault();
        const text = (e.clipboardData || window.clipboardData).getData('text');
        let cleanedText = text.replace(/[^а-яА-ЯёЁa-zA-Z\-\s]/g, '');
        cleanedText = cleanedText.replace(/\s+/g, ' ').trim();

        // Обрезаем до 3 слов
        const words = cleanedText.split(' ');
        if (words.length > 3) {
            cleanedText = words.slice(0, 3).join(' ');
        }

        this.value = cleanedText;
        validateFIO(this);
    });
}

// Запрет ввода цифр
function preventNumbers(event) {
    if (/\d/.test(event.key)) {
        event.preventDefault();
    }
}

// Валидация телефона
function validatePhone(field, countryCode) {
    const value = field.value.replace(/\D/g, '');

    if (countryCode === '+375' && value.length !== 9) {
        showFieldError(field, 'Белорусский номер: 9 цифр');
        return false;
    }

    if (countryCode === '+7' && value.length !== 10) {
        showFieldError(field, 'Российский номер: 10 цифр');
        return false;
    }

    clearFieldError(field);
    return true;
}

function validateTextField(field, minLength, maxLength, allowNumbers = false) {
    const value = field.value.trim();

    if (value.length < minLength) {
        showFieldError(field, `Минимум ${minLength} символов`);
        return false;
    }

    if (value.length > maxLength) {
        showFieldError(field, `Максимум ${maxLength} символов`);
        return false;
    }

    if (!allowNumbers && /\d/.test(value)) {
        showFieldError(field, 'Поле не может содержать цифры');
        return false;
    }

    // Проверка на специальные символы
    if (/[!@#$%^&*()_+=\[\]{};:"\\|<>/?`~]/.test(value)) {
        showFieldError(field, 'Недопустимые специальные символы');
        return false;
    }

    clearFieldError(field);
    return true;
}

function validateTitleWithNumbers(field, maxLength = 50) {
    const value = field.value.trim();

    if (value.length < 2) {
        showFieldError(field, 'Минимум 2 символа');
        return false;
    }

    if (value.length > maxLength) {
        showFieldError(field, `Максимум ${maxLength} символов`);
        return false;
    }

    if (!/^[а-яА-ЯёЁa-zA-Z0-9\s\(\)\-]+$/.test(value)) {
        showFieldError(field, 'Только буквы, цифры, дефис и скобки');
        return false;
    }

    clearFieldError(field);
    return true;
}

// Обновленная функция validateNumberField
function validateNumberField(field, min, max) {
    const value = parseInt(field.value);
    const strValue = field.value.trim();

    if (strValue === '') {
        showFieldError(field, 'Обязательное поле');
        return false;
    }

    if (strValue.length < 2 && strValue.length > 0) {
        showFieldError(field, 'Минимум 2 цифры');
        return false;
    }

    if (isNaN(value)) {
        showFieldError(field, 'Введите число');
        return false;
    }

    if (value < min) {
        showFieldError(field, `Минимальное значение: ${min}`);
        return false;
    }

    if (value > max) {
        showFieldError(field, `Максимальное значение: ${max}`);
        return false;
    }

    clearFieldError(field);
    return true;
}

// Функция для ограничения ввода только цифрами
function restrictNumberInput(input, min, max) {
    const maxLength = max.toString().length;
    input.maxLength = maxLength;

    input.addEventListener('keydown', function(e) {
        // Разрешаем управляющие клавиши
        if (e.key === 'Backspace' || e.key === 'Delete' || e.key === 'Tab' ||
            e.key === 'Enter' || e.key === 'ArrowLeft' || e.key === 'ArrowRight' ||
            e.ctrlKey || e.metaKey) {
            return true;
        }

        // Блокируем все кроме цифр
        if (!/^\d$/.test(e.key)) {
            e.preventDefault();
            return false;
        }

        // Проверяем, не превысит ли значение максимум
        const currentValue = this.value;
        const selectionStart = this.selectionStart;
        const selectionEnd = this.selectionEnd;
        const newValue = currentValue.substring(0, selectionStart) + e.key + currentValue.substring(selectionEnd);

        if (newValue.length > maxLength) {
            e.preventDefault();
            showFieldError(this, `Максимум ${maxLength} цифры`);
            return false;
        }
    });

    input.addEventListener('input', function() {
        // Удаляем все нецифровые символы
        this.value = this.value.replace(/\D/g, '');

        // Валидируем значение
        validateNumberField(this, min, max);
    });

    input.addEventListener('paste', function(e) {
        e.preventDefault();
        const text = (e.clipboardData || window.clipboardData).getData('text');
        const cleanedText = text.replace(/\D/g, '').substring(0, maxLength);

        this.value = cleanedText;
        validateNumberField(this, min, max);
    });
}

// Специальная функция для валидации цены (с поддержкой десятичных)
function restrictPriceInput(input, min, max) {
    const maxLength = max.toString().length + 3; // +3 для точки и 2 знаков после запятой

    input.addEventListener('keydown', function(e) {
        // Разрешаем управляющие клавиши
        if (e.key === 'Backspace' || e.key === 'Delete' || e.key === 'Tab' ||
            e.key === 'Enter' || e.key === 'ArrowLeft' || e.key === 'ArrowRight' ||
            e.ctrlKey || e.metaKey) {
            return true;
        }

        // Разрешаем одну точку для десятичных
        if (e.key === '.' && !this.value.includes('.')) {
            return true;
        }

        // Блокируем все кроме цифр
        if (!/^\d$/.test(e.key)) {
            e.preventDefault();
            return false;
        }

        // Проверяем длину целой части
        const parts = this.value.split('.');
        const integerPart = parts[0];

        // Если нет точки и целая часть уже 3 символа - блокируем
        if (!this.value.includes('.') && integerPart.length >= 3) {
            e.preventDefault();
            showFieldError(this, 'Максимум 300');
            return false;
        }
    });

    input.addEventListener('input', function() {
        // Удаляем все кроме цифр и точки
        let value = this.value.replace(/[^\d.]/g, '');

        // Убираем лишние точки
        const parts = value.split('.');
        if (parts.length > 2) {
            value = parts[0] + '.' + parts.slice(1).join('');
        }

        // Ограничиваем целую часть до 3 цифр
        if (parts[0].length > 3) {
            parts[0] = parts[0].substring(0, 3);
        }

        // Ограничиваем 2 знака после запятой
        if (parts.length === 2 && parts[1].length > 2) {
            value = parts[0] + '.' + parts[1].substring(0, 2);
        } else if (parts.length === 2) {
            value = parts[0] + '.' + parts[1];
        } else {
            value = parts[0];
        }

        this.value = value;
        validatePrice(this, min, max);
    });
}

// Функция для валидации названий миссий (с цифрами, тире и кавычками)
function validateMissionTitle(input) {
    const value = input.value.trim();

    if (value.length < 2) {
        showFieldError(input, 'Минимум 2 символа');
        return false;
    }

    if (value.length > 50) {
        showFieldError(input, 'Максимум 50 символов');
        return false;
    }

    // Проверка на недопустимые символы (разрешаем буквы, цифры, пробелы, тире и кавычки)
    if (!/^[а-яА-ЯёЁa-zA-Z0-9\s\-"']+$/.test(value)) {
        showFieldError(input, 'Только буквы, цифры, тире и кавычки');
        return false;
    }

    clearFieldError(input);
    return true;
}

// Функция для ограничения ввода в названиях миссий
function restrictMissionTitleInput(input) {
    input.maxLength = 50;

    input.addEventListener('keypress', function(e) {
        const char = String.fromCharCode(e.which || e.keyCode);

        // Разрешаем только буквы, цифры, пробелы, тире, и кавычки
        const pattern = /^[а-яА-ЯёЁa-zA-Z0-9\s\-"']$/;
        if (!pattern.test(char)) {
            e.preventDefault();
            return false;
        }
    });

    input.addEventListener('input', function() {
        // Удаляем недопустимые символы
        this.value = this.value.replace(/[^а-яА-ЯёЁa-zA-Z0-9\s\-"']/g, '');
        validateMissionTitle(this);
    });

    input.addEventListener('paste', function(e) {
        e.preventDefault();
        const text = (e.clipboardData || window.clipboardData).getData('text');
        const cleanedText = text.replace(/[^а-яА-ЯёЁa-zA-Z0-9\s\-"']/g, '');

        this.value = cleanedText.substring(0, 50);
        validateMissionTitle(this);
    });
}

function validatePrice(field, min, max) {
    const value = parseFloat(field.value);

    if (isNaN(value)) {
        showFieldError(field, 'Введите число');
        return false;
    }

    if (value < min) {
        showFieldError(field, `Минимальная цена: ${min}`);
        return false;
    }

    if (value > max) {
        showFieldError(field, `Максимальная цена: ${max}`);
        return false;
    }

    clearFieldError(field);
    return true;
}

// Функция для валидации названий с кавычками и тире
function validateExhibitionTitle(input) {
    const value = input.value.trim();

    if (value.length < 2) {
        showFieldError(input, 'Минимум 2 символа');
        return false;
    }

    if (value.length > 50) {
        showFieldError(input, 'Максимум 50 символов');
        return false;
    }

    // Проверка на недопустимые символы
    if (!/^[а-яА-ЯёЁa-zA-Z\s\-"']+$/.test(value)) {
        showFieldError(input, 'Только буквы, пробелы, тире и кавычки');
        return false;
    }

    clearFieldError(input);
    return true;
}

// Функция для ограничения ввода в названиях выставок
function restrictExhibitionTitleInput(input) {
    input.addEventListener('keypress', function(e) {
        const char = String.fromCharCode(e.which || e.keyCode);

        // Разрешаем только буквы, пробелы, тире, и кавычки
        const pattern = /^[а-яА-ЯёЁa-zA-Z\s\-"']$/;
        if (!pattern.test(char)) {
            e.preventDefault();
            return false;
        }
    });

    input.addEventListener('input', function() {
        // Удаляем недопустимые символы
        this.value = this.value.replace(/[^а-яА-ЯёЁa-zA-Z\s\-"']/g, '');
        validateExhibitionTitle(this);
    });

    input.addEventListener('paste', function(e) {
        e.preventDefault();
        const text = (e.clipboardData || window.clipboardData).getData('text');
        const cleanedText = text.replace(/[^а-яА-ЯёЁa-zA-Z\s\-"']/g, '');

        this.value = cleanedText;
        validateExhibitionTitle(this);
    });
}

// Инициализация валидации при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    // Валидация ФИО
    const fioFields = document.querySelectorAll('input[name="full_name"]');
    fioFields.forEach(field => {
        field.addEventListener('keypress', preventNumbers);
        field.addEventListener('input', () => validateFIO(field));
    });

    // Форматирование и валидация дат
    const dateFields = document.querySelectorAll('.date-input');
    dateFields.forEach(field => {
        field.addEventListener('input', function() {
            formatDateInput(this);
        });

        field.addEventListener('blur', function() {
            if (this.value.length === 10) {
                validateDate(this);
            }
        });
    });

    // Валидация текстовых полей
    const textFields = document.querySelectorAll('input[name="citizenship"], input[name="qualification"], input[name="theme"]');
    textFields.forEach(field => {
        field.addEventListener('input', () => {
            const value = field.value;
            if (/\d/.test(value)) {
                showFieldError(field, 'Поле не может содержать цифры');
            } else if (value.length > 0 && value.length < 2) {
                showFieldError(field, 'Минимум 2 символа');
            } else {
                clearFieldError(field);
            }
        });
    });

    const qualificationFields = document.querySelectorAll('input[name="qualification"]');
    qualificationFields.forEach(field => {
        field.addEventListener('input', () => validateTextField(field, 2, 70, false));
    });

    // Валидация названий
    const titleFields = document.querySelectorAll('input[name="title"]');
    titleFields.forEach(field => {
        field.addEventListener('input', () => {
            const maxLen = field.dataset.maxLength || 50;
            validateTextField(field, 2, maxLen, field.dataset.allowNumbers === 'true');
        });
    });

     // Валидация названий миссий (с цифрами)
    const missionTitles = document.querySelectorAll('#missionForm input[name="title"]');
    missionTitles.forEach(field => {
        field.addEventListener('input', () => validateTitleWithNumbers(field, 50));
    });

    // Валидация названий экспонатов (с цифрами и кавычками)
    const exhibitTitles = document.querySelectorAll('#exhibitForm input[name="title"]');
    exhibitTitles.forEach(field => {
        field.addEventListener('input', () => {
            const value = field.value.trim();
            if (value.length < 2) {
                showFieldError(field, 'Минимум 2 символа');
            } else if (value.length > 70) {
                showFieldError(field, 'Максимум 70 символов');
            } else if (!/^[а-яА-ЯёЁa-zA-Z0-9\s\(\)\"\-]+$/.test(value)) {
                showFieldError(field, 'Недопустимые символы');
            } else {
                clearFieldError(field);
            }
        });
    });
});