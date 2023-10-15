import requests
from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.response.history import HistoryResponse, HistoryResponseFactory
from managers.verify import VerifyManager
from server.depends import get_session

router = APIRouter(prefix="/verification", tags=['Payment'])


@router.post('/verify/')
async def get_my_payments(
    pdf_file: UploadFile = File(...)
):
    files = {'file': (pdf_file.filename, pdf_file.file)}
    response = requests.post('http://ml:7777/send', files=files)
    if response.status_code != 200:
        return {"status": "ML Address not correct"}
    response = response.json()
    if response['type'] == 'М-11':
        return await VerifyManager.verify_m11(file_data=response['file_data'])
    elif response['type'] == 'ФМУ-76':
        return await VerifyManager.verify_fmu76(file_data=response['file_data'])


@router.get('/docs', response_model=list[HistoryResponse])
async def get_docs(
    session: AsyncSession = Depends(get_session)
):
    data = await VerifyManager.get_history(session=session)

    return HistoryResponseFactory.get_from_models(data)