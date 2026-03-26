from website.models import Notification


def site_context(request):
    try:
        recent_notifications = Notification.objects.order_by('-timestamp')[:5]
        unread_count = Notification.objects.filter(is_read=False).count()
    except Exception:
        recent_notifications = []
        unread_count = 0
    return {
        'school_name': 'Greenwood International Academy',
        'recent_notifications': recent_notifications,
        'unread_count': unread_count,
    }
