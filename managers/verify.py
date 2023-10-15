import re

from api.request.fmu76 import fmu76Request
from api.request.m11 import m11Request

from datetime import datetime

# from deeppavlov import build_model, configs

from spellchecker import SpellChecker

from db.repository.history import HistoryRepository

# ner_model = build_model(configs.ner.ner_rus_bert, install=True, download=True)

spell = SpellChecker(language='ru')


class VerifyManager:

    @staticmethod
    def verify_organisation_name(name: str) -> dict:
        if not spell.correction(name) == name:
            return {
                'code': 400,
                'error_message': "Орфографическая ошибка",
                'recommendation': spell.candidates(name)
            }
        return {
            'status': 200,
        }

    @staticmethod
    def verify_act_number(act_numb: str) -> dict:
        act_number_pattern = r"^\d{8}$"

        if re.match(act_number_pattern, act_numb):
            if act_numb.isdigit():
                return {
                    'status': 200,
                }
            else:
                return {
                    'status': 400,
                    'error_message': "Найден недопустимый символ ",
                    'recommendation': 'В номере документа можно использовать только цифры'
                }
        else:
            return {
                'status': 400,
                'error_message': "Недопустимое кол-во симоволов ",
                'recommendation': 'Номер документа должен состоять из 8 символов'
            }

    @staticmethod
    def verify_organization_structure(org_struct: str, organisation_name: str) -> dict:
        if organisation_name not in org_struct:
            return {
                'status': 400,
                'error_message': "В структуре организации обязательно должно быть навзнаие организации"
            }
        if not spell.correction(org_struct) == org_struct:
            return {
                'code': 400,
                'error_message': "Орфографическая ошибка",
                'recommendation': spell.candidates(org_struct)
            }
        return {
            'status': 200,
        }

    @staticmethod
    def verify_act_date(act_date: str) -> dict:
        try:
            date_obj = datetime.strptime(act_date, "%d.%m.%Y")

            current_date = datetime.now()

            if date_obj <= current_date:
                return {
                    'status': 200
                }
            else:
                if not spell.correction(act_date) == act_date:
                    return {
                        'code': 400,
                        'error_message': "Орфографическая ошибка",
                        'recommendation': spell.candidates(act_date)
                    }
                return {
                    'status': 400,
                    'error_message': "Дата не может быть больше сегодняшней",
                    'recommendation': 'Укажите дату не превышающую сегодня'
                }
        except ValueError:
            return {
                'status': 400,
                'error_message': "Неправильно указан формат даты",
                'recomendation': 'Укажите дату в формате ДД/ММ/ГГГГ'
            }

    @staticmethod
    def verify_ocud_code(operation_code: str) -> dict:
        operation_code_pattern = r"^\d{7}$"

        if re.match(operation_code_pattern, operation_code):
            if operation_code.isdigit():
                if not spell.correction(operation_code) == operation_code:
                    return {
                        'code': 400,
                        'error_message': "Орфографическая ошибка",
                        'recommendation': spell.candidates(operation_code)
                    }
                return {
                    'status': 200,
                }
            else:
                return {
                    'status': 400,
                    'error_message': "Найден недопустимый символ ",
                    'recommendation': 'В ОКУД можно использовать только цифры'
                }
        else:
            return {
                'status': 400,
                'error_message': "Недопустимое кол-во симоволов ",
                'recommendation': 'ОКУД состоять из 7 символов'
            }

    @staticmethod
    def verify_okpo_code(okpo_code: str) -> dict:
        okpo_code_pattern = r"^\d{7}$"

        if re.match(okpo_code_pattern, okpo_code):
            if okpo_code.isdigit():
                return {
                    'status': 200,
                }
            else:
                return {
                    'status': 400,
                    'error_message': "Найден недопустимый символ ",
                    'recommendation': 'В ОКПО можно использовать только цифры'
                }
        else:
            return {
                'status': 400,
                'error_message': "Недопустимое кол-во симоволов ",
                'recommendation': 'ОКПО состоять из 7 символов'
            }

    @staticmethod
    def verify_operation_code(operation_code: str) -> dict:
        if operation_code.isdigit():
            return {
                'status': 200
            }
        elif operation_code == "-":
            return {
                'status': 200,
            }
        else:
            return {
                'status': 400,
                'error_message': "Найден недопустимый символ ",
                'recommendation': 'В операционном коде можно использовать только цифры'
            }

    @staticmethod
    def verify_sender_org(sender_org: str) -> dict:
        if not spell.correction(sender_org) == sender_org:
            return {
                'code': 400,
                'error_message': "Орфографическая ошибка",
                'recommendation': spell.candidates(sender_org)
            }
        return {
            'status': 200
        }

    @staticmethod
    def verify_tabl_numb(tabl_numb: str) -> dict:
        if '013' == tabl_numb or '014' == tabl_numb or '020' == tabl_numb or tabl_numb == "-":
            return {
                'status': 200,
            }
        return {
            'status': 400,
            'error_message': "Найден недопустимый символ ",
            'recommendation': 'В этом поле можно использовать только 014,020,013, -'
        }

    @staticmethod
    def verify_receiver_org_str(receiver_org_str: str):
        if not spell.correction(receiver_org_str) == receiver_org_str:
            return {
                'code': 400,
                'error_message': "Орфографическая ошибка",
                'recommendation': spell.candidates(receiver_org_str)
            }
        return {
            'status': 200
        }

    @staticmethod
    def verify_check(check: str) -> dict:
        if check.isdigit():
            return {
                'status': 200
            }
        else:
            return {
                'status': 400,
                'error_message': "Найден недопустимый символ ",
                'recommendation': 'В счете можно использовать только цифры'
            }

    @staticmethod
    def verify_analytic_report_code(analytic_report_code):
        if analytic_report_code.isdigit():
            return {
                'status': 200
            }
        else:
            return {
                'status': 400,
                'error_message': "Найден недопустимый символ ",
                'recommendation': 'В счете можно использовать только цифры'
            }

    @staticmethod
    def verify_accounting_unit(accounting_unit) -> dict:
        if not spell.correction(accounting_unit) == accounting_unit:
            return {
                'code': 400,
                'error_message': "Орфографическая ошибка",
                'recommendation': spell.candidates(accounting_unit)
            }
        return {
            'status': 200
        }

    @staticmethod
    def verify_person(person: str) -> dict:
        fio_pattern = re.compile(r'^[А-ЯЁа-яё]+\s[А-ЯЁа-яё]+\s[А-ЯЁа-яё]+$')
        if not fio_pattern.match(person):
            if not spell.correction(person) == person:
                return {
                    'code': 400,
                    'error_message': "Орфографическая ошибка",
                    'recommendation': spell.candidates(person)
                }
            return {
                'status': 400,
                'error_message': "Недопутсимый формат",
                'recommendation': 'Формат должен быть ФИО через пробел без сокращений'
            }
        # tokens, tags = ner_model([person])
        # names = [tokens[i] for i in range(len(tokens)) if 'B-PER' in tags[0][i]]
        # surnames = [tokens[i] for i in range(len(tokens)) if 'B-SUR' in tags[0][i]]
        # patronymics = [tokens[i] for i in range(len(tokens)) if 'B-PATR' in tags[0][i]]
        # if names == []:
        #     return {
        #         'status': 400,
        #         'error_message': "Имя не найденно",
        #         'recommendation': 'В ФИО Должно быть указано имя'
        #     }
        # elif surnames == []:
        #     return {
        #         'status': 400,
        #         'error_message': "Отчество не найденно",
        #         'recommendation': 'В ФИО Должно быть указано фамилия'
        #     }
        # elif patronymics == []:
        #     return {
        #         'status': 400,
        #         'error_message': 'Фамилия не найдена',
        #         'recommendation': 'В ФИО должно быть отчетсво'
        #     }
        return {
            'status': 200
        }

    @staticmethod
    def base_check(text: str) -> dict:
        if not spell.correction(text) == text:
            return {
                'code': 400,
                'error_message': "Орфографическая ошибка",
                'recommendation': spell.candidates(text)
            }
        return {
            'status': 200
        }

    @classmethod
    async def verify_m11(cls, file_data: m11Request):
        response = {}

        response['act_number'] = cls.verify_act_number(file_data.act_number)
        response['organization'] = cls.verify_organisation_name(file_data.organization)
        response['organization_structure'] = cls.verify_organization_structure(file_data.organization_structure,
                                                                               file_data.organization)
        response['ocud_code'] = cls.verify_ocud_code(file_data.ocud_code)
        response['okpo_code'] = cls.verify_okpo_code(file_data.okpo_code)
        response['code'] = cls.verify_operation_code(file_data.code)
        response['table1_act_date'] = cls.verify_act_date(file_data.table1[0].act_date)
        response['table1_operation_code'] = cls.verify_operation_code(file_data.table1[0].operation_code)
        response['table1_sender_org_str'] = cls.verify_sender_org(file_data.table1[0].sender_org_str)
        response['table1_sender_tabl_numb'] = cls.verify_tabl_numb(file_data.table1[0].sender_tabl_numb)
        response['table1_receiver_org_str'] = cls.verify_receiver_org_str(file_data.table1[0].receiver_org_str)
        response['table1_receiver_tabl_numb'] = cls.verify_tabl_numb(file_data.table1[0].sender_tabl_numb)
        response['table1_check'] = cls.verify_check(file_data.table1[0].check)
        response['table1_analytic_report_code'] = cls.verify_analytic_report_code(
            file_data.table1[0].analytic_report_code)
        response['table1_accounting_unit'] = cls.verify_accounting_unit(file_data.table1[0].accounting_unit)
        response['throw_person'] = cls.verify_person(file_data.throw_person)
        response['requested'] = cls.verify_person(file_data.requested)
        response['approved'] = cls.verify_person(file_data.approved)

        return response

    @classmethod
    async def verify_fmu76(cls, file_data: fmu76Request):
        response = {}

        response['act_number'] = cls.verify_act_number(file_data.act_number)
        response['organization'] = cls.verify_organisation_name(file_data.organization)
        response['organization_structure'] = cls.verify_organization_structure(file_data.organization_structure,
                                                                               file_data.organization)
        response['ocud_code'] = cls.verify_ocud_code(file_data.ocud_code)
        response['okpo_code'] = cls.verify_okpo_code(file_data.okpo_code)
        response['code_be'] = cls.verify_operation_code(file_data.code_be)
        response['boss'] = cls.verify_person(file_data.boss)
        response['sign_encode'] = cls.base_check(file_data.sign_encode)
        response['subdivision'] = cls.base_check(file_data.subdivision)
        response['operation_code'] = cls.verify_operation_code(file_data.operation_code)
        response['sender_org_str'] = cls.verify_sender_org(file_data.sender_org_str)
        response['check'] = cls.verify_check(file_data.check)
        response['expense_direction'] = cls.base_check(file_data.expense_direction)
        response['financially_responsible_person'] = cls.base_check(file_data.financially_responsible_person)

        return response

    @classmethod
    async def get_history(cls, session):
        return await HistoryRepository(session).history_all()
