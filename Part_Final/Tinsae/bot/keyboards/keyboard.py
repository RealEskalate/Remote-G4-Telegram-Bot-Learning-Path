from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


# Callback data for handling inline keyboard buttons
class ActionCallback(CallbackData, prefix="action"):
    command: str


# Inline keyboard with command buttons
commands_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[

        [ 
            InlineKeyboardButton(text="All Users", callback_data=ActionCallback(command="all_users").pack()),
            InlineKeyboardButton(text="Add Seller", callback_data=ActionCallback(command="add_seller").pack()),
        ], 
        [
            InlineKeyboardButton(text="Get User by ID", callback_data=ActionCallback(command="get_user_by_id").pack()),
            InlineKeyboardButton(text="Update User", callback_data=ActionCallback(command="update_user").pack()),
            InlineKeyboardButton(text="Delete User", callback_data=ActionCallback(command="delete_user").pack()),
        ],
    ]
)
commands_keyboard_foruser = InlineKeyboardMarkup(
    inline_keyboard=[
        [ 
            InlineKeyboardButton(text="reqister", callback_data=ActionCallback(command="add_user").pack()),
        ], 
       
    ]
)

commands_keyboard_after_reqistration = InlineKeyboardMarkup(
    inline_keyboard=[

        # [ 
        #     InlineKeyboardButton(text="Browse Products", callback_data=ActionCallback(command="browse_products").pack()),
        #     InlineKeyboardButton(text="View Cart", callback_data=ActionCallback(command="view_cart").pack()),
        # ], 
        # [
        #     InlineKeyboardButton(text="Order History", callback_data=ActionCallback(command="order_history").pack()),
        #     InlineKeyboardButton(text="Order Confirmation", callback_data=ActionCallback(command="order_confirmation").pack()),
        # ],
        #  [
        #     InlineKeyboardButton(text="Shipment Tracking", callback_data=ActionCallback(command="shipment_tracking").pack()),
        # ],





         [ 
            InlineKeyboardButton(text="Post Product", callback_data=ActionCallback(command="post_products").pack()),
            # InlineKeyboardButton(text="View order", callback_data=ActionCallback(command="view_order").pack()),
        ], 
        #  [
        #     InlineKeyboardButton(text="Shipment Tracking", callback_data=ActionCallback(command="shipment_tracking").pack()),
        # ],
    ]
)


