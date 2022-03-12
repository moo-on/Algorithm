from datetime import datetime


def solution(lines):
    time_series = []
    throughput = []
    for line in lines:
        date, time, duration = line.split()
        duration = float(duration.split("s")[0])
        end = ' '.join([date, time])
        end = datetime.timestamp(datetime.strptime(end, '%Y-%m-%d %H:%M:%S.%f'))
        start = end - float(duration) + 0.001
        time_series.append([start, end])
    time_series = sorted(time_series, key=lambda x: x[1])

    for i, time in enumerate(time_series):
        if i == len(time_series) - 1:
            throughput.append(1)  # 마지막 로그 끝나는 처리
            break
        end = time[1]
        cnt = 1
        for next_time in time_series[i + 1:]:
            next_start, next_end = next_time
            if next_end <= end + 1 - 0.001:  # 1초안에 새로운 로그 끝나는 경우
                cnt += 1
            elif next_end <= end + 4-0.002:  # 로그 최대 길이가 3인것을 이용하여 놓친 로그 처리량 체크
                if next_start <= end + 1 - 0.001:  # 시작 지점이 end +1 -0.001보다 작거나 같으면 조건 만족
                    cnt += 1
            else:
                throughput.append(cnt)
                cnt = 0
        throughput.append(cnt)

    return max(throughput)

print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
                "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
                "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s",
                "2016-09-15 21:00:02.066 2.62s"]))

print(solution([
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))
