from .models import Transaction
from .forms import FormDate
import logging

logger = logging.getLogger(__name__)

def transaction_filter(request, PARAMETERS_TRANSACTION):

    transact = Transaction.objects.all()
    form_date = FormDate()
    if 'user_date_start' in request.GET or 'user_date_end' in request.GET:
        form_date = FormDate(request.GET)
        if form_date.is_valid():
            start_date = form_date.cleaned_data.get('user_date_start')
            end_date = form_date.cleaned_data.get('user_date_end')
            if start_date:
                transact = transact.filter(date__gte=start_date)
            if end_date:
                transact = transact.filter(date__lte=end_date)
        else:
            transact = Transaction.objects.none()

    sort_param = request.GET.get('sort', '')
    sort_field = PARAMETERS_TRANSACTION.get(sort_param.lstrip('-'))
    if sort_field:
        prefix = ''
        if sort_param.startswith('-'):
            prefix = '-'
        transact = transact.order_by(prefix + sort_field, '-date')

    columns = [
        ('date', 'date'),
        ('title', 'title'),
        ('status__name_status', 'status'),
        ('operation_type__type_operation', 'operation_type'),
        ('categories__categories', 'categories'),
        ('subcategories__subcategories', 'subcategories'),
        ('amount', 'amount'),
        ('comment', 'comment'),
    ]
    query_fields = [query for query, _ in columns]
    query_fields_label = [query for _, query in columns]
    labels = [str(Transaction._meta.get_field(model_field).verbose_name)
              for _, model_field in columns]
    result = {
        'query_fields': query_fields,
        'labels': labels,
        'form_date': form_date,
        'transact': transact,
        'query_fields_label': query_fields_label,
    }

    return result