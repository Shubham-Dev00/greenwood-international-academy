from django.contrib import admin
from django.utils.html import format_html
from .models import (
    ContactMessage,
    Enquiry,
    FacultyMember,
    LeadershipMember,
    NewsEvent,
    Notification,
    PaymentRecord,
    Testimonial,
)

admin.site.site_header = "Greenwood Academy Administration"
admin.site.site_title = "Greenwood Admin"
admin.site.index_title = "School Dashboard"


@admin.action(description="Mark selected notifications as read")
def mark_notifications_read(modeladmin, request, queryset):
    queryset.update(is_read=True)


@admin.register(NewsEvent)
class NewsEventAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "event_date")
    search_fields = ("title", "category")
    list_filter = ("category", "event_date")
    ordering = ("-event_date",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role")
    search_fields = ("name", "role")


@admin.register(LeadershipMember)
class LeadershipMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "display_order")
    list_editable = ("display_order",)
    search_fields = ("name", "designation")
    ordering = ("display_order",)


@admin.register(FacultyMember)
class FacultyMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "department", "subject", "experience_years", "designation")
    list_filter = ("department",)
    search_fields = ("name", "subject", "designation")
    ordering = ("name",)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "timestamp", "read_badge")
    list_filter = ("category", "is_read", "timestamp")
    search_fields = ("title", "category")
    actions = (mark_notifications_read,)
    ordering = ("-timestamp",)

    def read_badge(self, obj):
        if obj.is_read:
            return format_html(
                '<span style="background:#198754;color:white;padding:4px 10px;border-radius:999px;font-weight:600;">Read</span>'
            )
        return format_html(
            '<span style="background:#dc3545;color:white;padding:4px 10px;border-radius:999px;font-weight:600;">Unread</span>'
        )

    read_badge.short_description = "Status"


@admin.register(PaymentRecord)
class PaymentRecordAdmin(admin.ModelAdmin):
    list_display = (
        "student_name",
        "class_section",
        "amount",
        "payment_method",
        "payment_date",
        "status_badge",
    )
    search_fields = ("student_name", "roll_number", "transaction_id")
    list_filter = ("payment_method", "payment_date", "status")
    ordering = ("-payment_date",)

    def status_badge(self, obj):
        color_map = {
            "Paid": "#198754",
            "Pending": "#ffc107",
            "Failed": "#dc3545",
            "Success": "#198754",
        }
        color = color_map.get(str(obj.status), "#0d6efd")
        return format_html(
            '<span style="background:{};color:white;padding:4px 10px;border-radius:999px;font-weight:600;">{}</span>',
            color,
            obj.status,
        )

    status_badge.short_description = "Status"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "email", "created_at")
    search_fields = ("name", "email", "subject")
    list_filter = ("subject", "created_at")
    ordering = ("-created_at",)


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        "student_name",
        "applying_class",
        "preferred_session",
        "reference_number",
        "created_at",
    )
    search_fields = ("student_name", "reference_number", "email")
    list_filter = ("applying_class", "preferred_session", "created_at")
    ordering = ("-created_at",)