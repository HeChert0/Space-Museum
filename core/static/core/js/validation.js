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

function validateFIO(field) {
    const value = field.value.trim();

    if (value.length < 2) {
        showFieldError(field, 'ФИО должно содержать минимум 2 символа');
        return false;
    }

    if (value.length > 50) {
        showFieldError(field, 'ФИО не может быть длиннее 50 символов');
        return false;
    }

    if (/\d/.test(value)) {
        showFieldError(field, 'ФИО не может содержать цифры');
        return false;
    }

    if (/[!@#$%^&*()_+=\[\]{};:"\\|,.<>/?`~]/.test(value)) {
        showFieldError(field, 'ФИО не может содержать специальные символы');
        return false;
    }

    const words = value.split(/\s+/);
    if (words.length < 2) {
        showFieldError(field, 'Введите имя и фамилию');
        return false;
    }

    clearFieldError(field);
    return true;
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

// Валидация числовых полей
function validateNumberField(field, min, max) {
    const value = parseInt(field.value);

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
