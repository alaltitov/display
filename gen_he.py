# -*- coding: utf-8 -*-
"""Generate translations/he.yaml in LOGICAL Hebrew order.

The firmware build enables LV_USE_BIDI=1 (see main.yaml platformio_options),
so LVGL performs the bidirectional reordering at render time. Therefore the
translations are stored in natural LOGICAL Hebrew order (human-readable and
maintainable) - do NOT pre-reverse them.
"""
import io

# Logical-order Hebrew translations (natural, human-readable Hebrew).
T = [
    ("loading", [
        ("synchronization", "מסנכרן..."),
        ("connection_api", "מתחבר לשרת..."),
    ]),
    ("ota", [
        ("start", [
            ("primary", "מתחיל עדכון!"),
            ("secondary", "המתן..."),
        ]),
        ("end", [
            ("primary", "העדכון הושלם!"),
            ("secondary", "מאתחל..."),
        ]),
        ("error", [
            ("primary", "שגיאת עדכון!"),
            ("secondary", "מאתחל..."),
        ]),
        ("progress", "התקדמות קושחה %0.1f%%"),
    ]),
    ("settings", [
        ("backlight", "תאורת רקע"),
        ("sleep_time", "זמן כיבוי"),
    ]),
    ("sleep_time", [
        ("never", "לעולם לא"),
        ("minute1", "דקה אחת"),
        ("minute5", "5 דקות"),
        ("minute10", "10 דקות"),
        ("minute30", "30 דקות"),
        ("hour1", "שעה אחת"),
        ("hour6", "6 שעות"),
        ("hour12", "12 שעות"),
    ]),
    ("forecasts", [
        ("daily", "יומי"),
        ("hourly", "שעתי"),
    ]),
    ("weather", [
        ("clear-night", "בהיר בלילה"),
        ("cloudy", "מעונן"),
        ("exceptional", "חריג"),
        ("fog", "ערפל"),
        ("hail", "ברד"),
        ("lightning", "ברקים"),
        ("lightning-rainy", "ברקים וגשם"),
        ("partlycloudy", "מעונן חלקית"),
        ("pouring", "גשם שוטף"),
        ("rainy", "גשום"),
        ("snowy", "שלג"),
        ("snowy-rainy", "שלג וגשם"),
        ("sunny", "שמשי"),
        ("windy", "רוחות"),
        ("windy-variant", "רוחות ועננים"),
    ]),
    ("day_of_week", [
        ("monday", "יום שני"),
        ("tuesday", "יום שלישי"),
        ("wednesday", "יום רביעי"),
        ("thursday", "יום חמישי"),
        ("friday", "יום שישי"),
        ("saturday", "שבת"),
        ("sunday", "יום ראשון"),
    ]),
    ("day_of_week_short", [
        ("monday", "ב׳"),
        ("tuesday", "ג׳"),
        ("wednesday", "ד׳"),
        ("thursday", "ה׳"),
        ("friday", "ו׳"),
        ("saturday", "ש׳"),
        ("sunday", "א׳"),
    ]),
    ("month", [
        ("january", "ינואר"),
        ("february", "פברואר"),
        ("march", "מרץ"),
        ("april", "אפריל"),
        ("may", "מאי"),
        ("june", "יוני"),
        ("july", "יולי"),
        ("august", "אוגוסט"),
        ("september", "ספטמבר"),
        ("october", "אוקטובר"),
        ("november", "נובמבר"),
        ("december", "דצמבר"),
    ]),
    ("vacuum", [
        ("name", "שואב אבק"),
        ("state", [
            ("cleaning", "מנקה"),
            ("docked", "בעמדת עגינה"),
            ("error", "שגיאה"),
            ("idle", "במנוחה"),
            ("off", "כבוי"),
            ("on", "פועל"),
            ("paused", "מושהה"),
            ("returning", "חוזר לעמדה"),
        ]),
    ]),
    ("cover", [
        ("name", "תריס"),
        ("state", [
            ("closed", "סגור"),
            ("closing", "נסגר"),
            ("open", "פתוח"),
            ("opening", "נפתח"),
            ("stopped", "עצור"),
        ]),
    ]),
    ("alarm_panel", [
        ("name", "לוח בקרת אזעקה"),
        ("enter_pass", "הזן סיסמה"),
        ("wrong_pass", "סיסמה שגויה"),
        ("state", [
            ("armed", "דרוך"),
            ("armed_away", "דרוך ביציאה"),
            ("armed_custom_bypass", "דריכה מותאמת"),
            ("armed_home", "דרוך בבית"),
            ("armed_night", "דרוך בלילה"),
            ("armed_vacation", "דרוך בחופשה"),
            ("arming", "מפעיל דריכה"),
            ("disarmed", "מנוטרל"),
            ("disarming", "מנטרל"),
            ("pending", "ממתין"),
            ("triggered", "הופעל"),
        ]),
    ]),
    ("fan", [
        ("name", "מאוורר"),
        ("state", [
            ("on", "כבוי"),
            ("off", "פועל"),
        ]),
    ]),
]


def emit(items, indent, out, quote_onoff=False):
    pad = "  " * indent
    for key, val in items:
        k = '"%s"' % key if (quote_onoff and key in ("on", "off")) else key
        if isinstance(val, list):
            out.write("%s%s:\n" % (pad, k))
            emit(val, indent + 1, out, quote_onoff)
        else:
            out.write('%s%s: "%s"\n' % (pad, k, val))


buf = io.StringIO()
buf.write("# Hebrew (he) translation.\n")
buf.write("# Stored in LOGICAL order; the firmware build enables LV_USE_BIDI=1 so\n")
buf.write("# LVGL handles right-to-left reordering at render time.\n")
buf.write("# Regenerate with gen_he.py instead of editing by hand.\n")
first = True
for key, val in T:
    if not first:
        buf.write("\n")
    first = False
    buf.write("%s:\n" % key)
    emit(val, 1, buf, quote_onoff=(key == "fan"))

with open("src/translations/he.yaml", "w", encoding="utf-8", newline="\n") as f:
    f.write(buf.getvalue())

print("WROTE translations/he.yaml (logical order)")
