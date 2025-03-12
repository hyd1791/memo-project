from django.shortcuts import render,redirect,get_object_or_404
from .models import Note
from .forms import NoteForm
# Create your views here.
# 메모 목록을 띄우는 코드
def note_list(request):
    notes = Note.objects.all()
    #render: html 파일과 연결하겠다
    return render(request, 'notes/note_list.html', {'notes':notes})
#메모장 생성
def note_create(request):
    #사용자 폼을 post형식으로 받아야한다
    #사용자가 메모장을 생성했을때 웹 GET,은 보안위협이 일을수있어 POST로 받아야한다.
    if request.method == 'POST':
        form = Noteform(request.POST)
        #폼 형식을 받을 때는 유효성 검사 (보안) 
        if form.is_valid():  #유효성 검사
            form.save() #데이터베이스 저장. 
    #redirect('url'): url 주소로 이동
            return redirect('note_list') # 목록으로 이동               
    else: #처음 들어왔을 때
        form = NoteForm()
        return render(request,'notes/note_create.html',{'form':form})

#메모장 상세보기
def note_detail(request,pk):  #pk는 리스트 하나하나에 부여된 고유숫자
    note = get_object_or_404(Note,pk=pk)
    return render(request, 'notes/note_detail.html',{"note":note})