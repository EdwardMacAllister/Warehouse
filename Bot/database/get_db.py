from Bot.handlers.auth.user_authentication_handler import UserActionsStates


@router.message(UserActionsStates.waiting_for_username_password)
async def process_create_user(message: types.Message, state: FSMContext):
    """Process the username and password input for creating a new user."""
    args = message.text.split()

    if len(args) < 2:
        await message.reply("Пожалуйста, введите имя пользователя и пароль.")
        return

    username = args[0]
    password = args[1]

    # Use get_db as a context manager
    with get_db() as db:
        try:
            existing_user = db.query(User).filter(User.username == username).first()
            if existing_user:
                await message.reply("Имя пользователя уже существует.")
                return

            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            new_user = User(username=username, password_hash=password_hash)
            db.add(new_user)
            db.commit()
            await message.reply(f"Пользователь {username} создан.", reply_markup=user_menu_keyboard())
        except Exception as e:
            logging.error(f"Error adding user: {e}")
            await message.reply("Ошибка при создании пользователя.")
