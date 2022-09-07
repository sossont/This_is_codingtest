# 걸린 시간 :40분
# 문자열 처리하는데에 애먹었다.

def solution(m, musicinfos):
    max_length = 0
    codes = []
    names = []
    length = []
    answer_idx = -1

    # 입력 처리
    for music in musicinfos:
        start_hour = int(music[0:2]) * 60
        start_min = int(music[3:5])
        end_hour = int(music[6:8]) * 60
        end_min = int(music[9:11])
        running_time = (end_hour - start_hour) + (end_min - start_min)
        musics = music[12:]
        full_musics = musics.split(',')
        music_name = full_musics[0]
        full_music = full_musics[1]
        music_code = []
        code_idx = -1
        for i in range(len(full_music)):
            if full_music[i] == '#':
                music_code[code_idx] += "#"
            else:
                music_code.append(full_music[i])
                code_idx += 1

        code_len = len(music_code)
        code = []
        real_time = 0
        while True:
            if real_time == running_time:
                break
            code.append(music_code[real_time % code_len])
            real_time += 1

        names.append(music_name)
        codes.append(code)
        length.append(running_time)

    code_idx = -1
    real_m = []
    for i in range(len(m)):
        if m[i] == '#':
            real_m[code_idx] += "#"
        else:
            real_m.append(m[i])
            code_idx += 1
    # 문제 푸는 부분

    for i in range(len(names)):
        mlen = len(real_m)
        for j in range(len(codes[i])):
            midx = 0
            while j + midx < len(codes[i]):
                if codes[i][j + midx] == real_m[midx]:
                    midx += 1
                else:
                    break

                if midx == mlen:
                    break

            if midx == mlen:
                if length[i] > max_length:
                    max_length = length[i]
                    answer_idx = i

    # A# -> G,
    if answer_idx == -1:
        return "(None)"
    else:
        return names[answer_idx]