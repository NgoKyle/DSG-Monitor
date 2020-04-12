from discord_webhook import DiscordWebhook

def sendDiscord(message, buyType, sku, condition):
    #default error url
    if "curbside" in buyType:
        if sku in ('16380346', '11465449', '16122502', '14659184'): #adjustable
            if condition in '97236': #pdx
                url = 'https://discordapp.com/api/webhooks/696488049336385586/TJvbPriFLk6tCX57sLqb_DEfU5nw1DxD_PSJ3LHaeqhDEu7NACN8EePLGNoZ2yx6NMFR'
            elif condition in '98101': #sea
                url = 'https://discordapp.com/api/webhooks/697145833908338839/yYcNa3Kp60ymQ8guITMJbC3Nw-Hj6d5v-_QaWMpvmPQQ7zO_a5R9jCLqeIRE9DIFTARS'
            elif condition in '99201': #spok
                url = 'https://discordapp.com/api/webhooks/697145930612474007/BuYoVBFTpBAkovHYyXgobnu2Y-iMdHJb7VEh11XOONAe2z_gnBiuD5NntFnGYEecgFlh'
            elif condition in '97701': #bend
                url = 'https://discordapp.com/api/webhooks/697146053409112266/1_QjYxznO04s4-M3A6oME8GYuHA8RscTj6IoilZm3zpCEwxWN-iZlro66RL4jobJJDxF'
            else: #adjustable - everywhere
                url = 'https://discordapp.com/api/webhooks/697209785308807200/N43rRgJLgO-BgXhue9WY3Bs5tFlJTE-m6SXnqjRJRHJ0Qp_xoC0l6h0H5enu3WkaY5rA'

        else:
            if condition in '97236': #fixed - pdx
                url = 'https://discordapp.com/api/webhooks/696488119364747274/akRhi50mQwDDVBrydTNUMd-m-7V4JH1D6ZHUz5cP2Sdft30BH1oee23x1A7FowoxB_LU'
            else: #fixed-everywhere
                url = 'https://discordapp.com/api/webhooks/698737074563579945/RYBK2jOi9orZA-ajVK2nE9MBqctbL17HhXLYBG76kJ1Y4oZm16OkqNtu4oBOZbCFbszR'
    elif "online" in buyType:
        if condition in 'inventory':
            if sku in ('16380346', '11465449', '16122502', '14659184'): #adjustable-inventory
                url = 'https://discordapp.com/api/webhooks/697503879457407018/TCpMS4Z-L-yMcQ_xtFF8tEmOdrppm6x8hUFdrrYPC2QR1x4qwsa9cLDS2Qfmnb5PtFau'
            else: #fixed-inventory
                url = 'https://discordapp.com/api/webhooks/697504568271044628/7mBmV_PVYURI48kXlvh2WxLjL9HWZ-W77M_R_lRKJsrlkwGsFs-oVoYLk_KRuMN3Noqu'
        elif condition in 'version1':
            if sku in ('16380346', '11465449', '16122502', '14659184'): #adjustable-1
                url = 'https://discordapp.com/api/webhooks/697504220919758880/-I4uF8_QKslDVw4JOOiCbqy5LOooz5ImwbFFq8bpUKQuqp6MvdIJhg5nWcExVh32awXX'
            else: #fixed-1
                url = 'https://discordapp.com/api/webhooks/697505503936249857/scMnb58LVNrIljlV7OViGecU86DiXr3AZ-x8aUnfT-_0Tz5wKjZE0qc-NLx5Go_bNiYB'
        elif condition in 'version2':
            if sku in ('16380346', '11465449', '16122502', '14659184'): #adjustable-2
                print("NOT HERE")
                url = 'https://discordapp.com/api/webhooks/697506746679296050/wg7i31v4MLisztQDeYwuPXcejgb_afz7JYq9qWf0qScQLRwURkt0AKeGZ6LMG6g63DpK'
            else: #fixed-2
                print("HEREE")
                url = 'https://discordapp.com/api/webhooks/697506942251171882/5OEwM50JV5MOCd7XqoWN1Z81JZas-SqU_cr9rToShhhVx6m5qqFvd-lnIGcP9swnyg35'
        elif condition in 'version3':
            if sku in ('16380346', '11465449', '16122502', '14659184'): #adjustable3
                url = 'https://discordapp.com/api/webhooks/697506842321879062/cevIveTTOBnIYtQIRKP82fnZVipdK0PgJ796lvzsjDbacyqYadRMBBhzt09jk2V87t_o'
            else: #fixed-3
                url = 'https://discordapp.com/api/webhooks/697507023549497437/Wkf_tLa5ccHWD8ZOYNkSGumPT2x0GfJQUagTjNn55aIrWh_lF8P8eXSbg8BvrxsSHuNH'
        elif condition in 'version4':
            url = 'https://discordapp.com/api/webhooks/698442217416687626/GhpCIxZJQeOwBW3EDcXHL3ZG9JEZ97bgWyzl-GlirwXrg0jkJxOpiJvgBmnw6jhjbeqb'
        else: #online-error
            url = 'https://discordapp.com/api/webhooks/697505663085052014/sU4e4VInVfvWZ_xRtv8aGY5WCu3e1b3c9Xr41_JtIuu9UKpTOTFcYRoW6vi1N9BnDOsm'


    else:
        url = 'https://discordapp.com/api/webhooks/697146323924811856/2POHtN42U2ouMp3loe4u704JwspP9vxwpPNdtFGlqpaLw8rSEmldq4f71gKTTU_wwrcP'

    webhook = DiscordWebhook(url=url,content=message)
    webhook.execute()
