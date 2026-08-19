class RegisterFromRoomPayload(BaseModel):
    owner_session: str
    owner_token: Optional[str] = None
    frontend_base: Optional[str] = None
    initial: Optional[dict] = None


@app.post('/api/rooms/register_from_room')
async def register_from_room(payload: RegisterFromRoomPayload, request: Request):
    # verify owner token
    await require_token_for_session(payload.owner_session, None, payload.owner_token)
    new_session = generate_session_id()
    new_token = generate_token()
    state = payload.initial if payload.initial is not None else {"objects": []}
    await save_room_state(new_session, state, token=new_token)

    # build frontend URL — prefer explicit frontend_base if provided
    if payload.frontend_base:
        base = payload.frontend_base.rstrip('/')
    else:
        # request.base_url points to API base; may differ from frontend host
        base = str(request.base_url).rstrip('/')

    url = f"{base}/web/ai-space/index.html?session={new_session}&token={new_token}"
    return {"session": new_session, "token": new_token, "url": url}
