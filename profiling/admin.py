from django.contrib import admin
from .models import PrakritiQuestion, PatientResponse, FoodPreference

@admin.register(PrakritiQuestion)
class PrakritiQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text_short', 'dosha', 'id')
    list_filter = ('dosha',)
    search_fields = ('question_text', 'dosha')
    ordering = ('dosha', 'id')

    def question_text_short(self, obj):
        return obj.question_text[:80] + '...' if len(obj.question_text) > 80 else obj.question_text
    question_text_short.short_description = 'Question'

@admin.register(PatientResponse)
class PatientResponseAdmin(admin.ModelAdmin):
    list_display = ('patient', 'question_short', 'answer', 'dosha')
    list_filter = ('answer', 'question__dosha')
    search_fields = ('patient__user__username', 'question__question_text')
    raw_id_fields = ('patient', 'question')

    def question_short(self, obj):
        return obj.question.question_text[:50] + '...' if len(obj.question.question_text) > 50 else obj.question.question_text
    question_short.short_description = 'Question'
    question_short.admin_order_field = 'question__question_text'

    def dosha(self, obj):
        return obj.question.dosha
    dosha.short_description = 'Dosha'
    dosha.admin_order_field = 'question__dosha'

@admin.register(FoodPreference)
class FoodPreferenceAdmin(admin.ModelAdmin):
    list_display = ('patient', 'food_name', 'preference_type', 'id')
    list_filter = ('preference_type',)
    search_fields = ('patient__user__username', 'food_name', 'preference_type')
    raw_id_fields = ('patient',)
