# Clinic Appointments
Микросервис для записи пациентов к врачу с полной документацией, тестами и CI/CD.
Проект был доработан до идеального состояния: исправлены ошибки, улучшена структура, оформлена документация 
и автоматизированы проверки.

## Запуск...

```bash
git clone ...
cd clinic_appointments
cp .env.example .env
docker-compose up -d --build
curl localhost:8000/health
